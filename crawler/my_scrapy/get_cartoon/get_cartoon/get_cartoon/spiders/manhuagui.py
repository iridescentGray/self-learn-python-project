import scrapy

from ..items import MhgChapterItem


class ManhuaguiSpider(scrapy.Spider):
    name = "manhuagui"

    def __init__(self):
        self.allowed_domains = ['www.manhuagui.com']
        self.start_urls = ['https://www.manhuagui.com/comic/1769/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response, **kwargs):
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
            chapter_item['page_number'] = chapters_selector.xpath('a[1]/span/i/text()').extract_first()
            chapter_items.append(chapter_item)

        for chapter_item in chapter_items:
            yield scrapy.Request(url=chapter_item['url'], meta={'item': chapter_item},
                                 callback=self.parse_every_chapter)

    def parse_every_chapter(self, response):
        pass


    # def parse_every_page(self, response):
    #     # 接收传递的item
    #     item = response.meta['item']
    #     # 获取该页面的链接
    #     item['link_url'] = response.url
    #     hxs = Selector(response)
    #     pre_img_url = hxs.xpath('//script/text()').extract()
    #     # 注意这里返回的图片地址,应该为列表,否则会报错
    #     img_url = [self.server_img + re.findall(self.pattern_img, pre_img_url[0])[0]]
    #     # 将获取的图片链接保存到img_url中
    #     item['img_url'] = img_url
    #     # 返回item，交给item pipeline下载图片
    #     yield item
