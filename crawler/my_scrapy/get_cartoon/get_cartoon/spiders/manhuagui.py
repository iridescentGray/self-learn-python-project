import time
from urllib.parse import quote

import scrapy

from get_cartoon.items import MhgChapterItem


def bond_path_to_url(url, path) -> str:
    """
    拼接url与所带参数
    :param url: {str} 链接
    :param path: {str} 参数
    :return: {str} 拼接后的url
    """
    str_encode = quote(path)
    return url + str_encode


domain = 'https://www.manhuagui.com'


class ManhuaguiSpider(scrapy.Spider):
    name = "manhuagui"
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 3,
        'COOKIES_ENABLED': False,
        'PLAYWRIGHT_BROWSER_TYPE': 'chromium',
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": False,
            "timeout": 10 * 1000,  # 10 seconds
        }
    }

    def __init__(self, **kwargs):
        self.allowed_domains = ['manhuagui.com']
        self.start_urls = ['https://www.manhuagui.com/comic/22265/']
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
            chapter_item['name'] = chapters_selector.xpath('a[1]/@title').extract_first()
            chapter_item['url'] = chapters_selector.xpath('a[1]/@href').extract_first()
            chapter_item['page_number'] = chapters_selector.xpath('a[1]/span/i/text()').extract_first().removesuffix(
                'p')
            chapter_items.append(chapter_item)

        i = 0
        for chapter_item in chapter_items:
            i = i + 1
            if i >= 2:
                continue
            print("chapter_item" + str(chapter_item))
            time.sleep(1)
            yield scrapy.Request(url=bond_path_to_url(domain, chapter_item['url']),
                                 meta={'item': chapter_item},
                                 callback=self.parse_every_chapter_pages)

    def parse_every_chapter_pages(self, response):
        chapter_item = response.meta['item']
        pages = int(chapter_item['page_number'])
        print("pages is %s" % pages)

        i = 0
        for page in range(1, pages, 1):
            i = i + 1
            if i >= 5:
                continue
            page_url = bond_path_to_url(domain, chapter_item['url']) + f'#p={str(page)}'
            print(page_url)
            yield scrapy.Request(url=page_url,
                                 meta=dict(
                                     item='item',
                                     playwright=True,
                                     playwright_include_page=True
                                 ),
                                 callback=self.parse_image_url,
                                 dont_filter=True,
                                 errback=self.errback_close_page)

    async def parse_image_url(self, response):
        print("parse_every_images is %s")

        page = response.meta["playwright_page"]
        await page.close()
        image_path = response.xpath('//*[@id="mangaFile"]/@src').extract_first()
        print(f"image_path is {image_path}")
        chapter_item = response.meta['item']
        chapter_item['image_paths'] = image_path

        yield chapter_item

    async def errback_close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
