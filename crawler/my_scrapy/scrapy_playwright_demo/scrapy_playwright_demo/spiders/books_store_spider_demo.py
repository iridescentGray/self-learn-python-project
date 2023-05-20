import hashlib
import logging
from pathlib import Path
from typing import Generator, Optional

from scrapy import Spider
from scrapy.http.response import Response


# run command: scrapy crawl books_store_spider_demo
class BooksSpider(Spider):
    """
    Extract all books, save screenshots.
    """

    name = "books_store_spider_demo"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "CONCURRENT_REQUESTS": 16,
        "PLAYWRIGHT_MAX_PAGES_PER_CONTEXT": 4,
        "CLOSESPIDER_ITEMCOUNT": 100,
        "FEEDS": {
            "books.json": {"format": "json", "encoding": "utf-8", "indent": 4},
        },
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": True,
            "timeout": 15 * 1000,  # 15 seconds
        },
    }
    start_urls = ["http://books.toscrape.com"]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        logging.getLogger("scrapy.core.engine").setLevel(logging.WARNING)
        logging.getLogger("scrapy.core.scraper").setLevel(logging.WARNING)

    def parse(self, response: Response, current_page: Optional[int] = None) -> Generator:
        page_count = response.css(".pager .current::text").re_first(r"Page \d+ of (\d+)")
        page_count = int(page_count)
        for page in range(2, page_count + 1):
            yield response.follow(f"/catalogue/page-{page}.html", cb_kwargs={"current_page": page})

        current_page = current_page or 1
        for book in response.css("article.product_pod a"):
            yield response.follow(
                book,
                callback=self.parse_book,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": f"page-{current_page}",
                },
            )

    async def parse_book(self, response: Response) -> dict:
        url_sha256 = hashlib.sha256(response.url.encode("utf-8")).hexdigest()
        page = response.meta["playwright_page"]
        await page.wait_for_load_state("domcontentloaded")
        await page.screenshot(path=Path(__file__).parent / "books" / f"{url_sha256}.png", full_page=True)
        await page.close()
        return {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "price": response.css("p.price_color::text").get(),
            "breadcrumbs": response.css(".breadcrumb a::text").getall(),
            "image": f"books/{url_sha256}.png",
        }
