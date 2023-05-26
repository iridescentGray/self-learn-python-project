# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from pydantic import BaseModel


# Have Be Verified，pydantic Can be replaced scrapy Native Item
class DoubanItem(BaseModel):
    title: str
    score: str
    motto: str | None

# scrapy Native Item
# class DoubanItem(scrapy.Item):
#     title = scrapy.Field()
#     score = scrapy.Field()
#     motto = scrapy.Field()
