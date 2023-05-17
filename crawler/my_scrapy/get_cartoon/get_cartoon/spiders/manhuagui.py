import scrapy

from get_cartoon.items import MhgChapterItem

domain = "https://www.manhuagui.com"


class ManhuaguiSpider(scrapy.Spider):
    name = "manhuagui"
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "CONCURRENT_REQUESTS": 4,
        "DOWNLOAD_DELAY": 3,
        "COOKIES_ENABLED": False,
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": True,
            "timeout": 15 * 1000,  # 15 seconds
        },
        'ITEM_PIPELINES': {
            "get_cartoon.pipelines.MhgChapterPipeline": 1,
        },
    }

    def __init__(self, **kwargs):
        self.allowed_domains = ["manhuagui.com"]
        self.start_urls = ["https://www.manhuagui.com/comic/22265/"]
        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        # 获取章节列表，单个章节的xpath是：  //*[@id="chapter-list-0"]/ul/li[1]/a
        # <a href="/comic/1769/669360.html" title="第371话试看"  target="_blank"><span>第371话试…<i>18p</i></span></a>

        # 两种方式，可以用xpath，也可用css
        chapters_selectors = response.xpath('//*[@id="chapter-list-0"]/ul/li')
        # chapters_selectors = response.css('#chapter-list-0 > ul > li')

        chapter_items = []
        for chapters_selector in chapters_selectors:
            chapter_item = MhgChapterItem()
            chapter_item["name"] = chapters_selector.xpath(
                "a[1]/@title"
            ).extract_first()
            chapter_item["url"] = chapters_selector.xpath("a[1]/@href").extract_first()
            chapter_item["page_number"] = (
                chapters_selector.xpath("a[1]/span/i/text()")
                .extract_first()
                .removesuffix("p")
            )
            chapter_item["web_image_items"] = {}
            chapter_items.append(chapter_item)

        for chapter_item in chapter_items:
            yield scrapy.Request(
                url=f'{domain}/{chapter_item["url"]}',
                meta={"item": chapter_item},
                callback=self.parse_every_chapter_pages,
            )

    def parse_every_chapter_pages(self, response):
        chapter_item = response.meta["item"]
        pages = int(chapter_item["page_number"])
        for page in range(1, pages, 1):
            page_url = f'{domain}/{chapter_item["url"]}#p={str(page)}'
            yield scrapy.Request(
                url=page_url,
                meta=dict(
                    item=chapter_item,
                    current_page=page,
                    playwright=True,
                    playwright_include_page=True,
                ),
                callback=self.parse_image_url,
                dont_filter=True,
                errback=self.errback_close_page,
            )

    async def parse_image_url(self, response):
        # if playwright_include_page=True,The following 'playwright_page' attributes can be obtain
        web_page = response.meta["playwright_page"]
        # wait page loading complete
        await web_page.close()
        current_page_number = response.meta["current_page"]
        image_path = response.xpath('//*[@id="mangaFile"]/@src').extract_first()
        chapter_item = response.meta["item"]
        # {漫画页数：漫画路径}
        chapter_item["web_image_items"].update({current_page_number: image_path})
        yield chapter_item

    async def errback_close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
