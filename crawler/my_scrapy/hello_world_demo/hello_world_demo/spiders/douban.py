import scrapy
from scrapy import Selector, Request

from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}')

    def parse(self, response, **kwargs):
        sel = Selector(response)
        movie_items = sel.css('#content > div > div.article > ol > li')

        for movie_sel in movie_items:
            item = DoubanItem()
            item['title'] = movie_sel.css('.title::text').extract_first()
            item['score'] = movie_sel.css('.rating_num::text').extract_first()
            item['motto'] = movie_sel.css('.inq::text').extract_first()
            yield item
