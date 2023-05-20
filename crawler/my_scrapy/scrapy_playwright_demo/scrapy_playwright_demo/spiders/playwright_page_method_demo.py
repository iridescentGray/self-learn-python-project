from pathlib import Path

import scrapy
from scrapy_playwright.page import PageMethod


# run command: scrapy crawl playwright_page_method_demo
class PlaywrightPageMethodDemo(scrapy.Spider):
    """
    All Method Playwright Support,see follow doc:
    https://playwright.dev/python/docs/api/class-page
    """
    name = "playwright_page_method_demo"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://example.org",
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    # Take a screenshot of the page
                    PageMethod("screenshot", path=Path(__file__).parent / "send_post_request.png", full_page=True),
                    # same effect code as:
                    # async def parse(self, response):
                    #     page = response.meta["playwright_page"]
                    #     screenshot = await page.screenshot(path="example.png", full_page=True)
                    #     # screenshot contains the image's bytes
                    #     await page.close()
                ]
            }
        )

    def parse(self, response, **kwargs):
        yield None
