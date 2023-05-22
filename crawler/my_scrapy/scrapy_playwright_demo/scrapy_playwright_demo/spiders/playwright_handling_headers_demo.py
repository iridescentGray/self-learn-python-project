import json
from pathlib import Path

import scrapy
from scrapy_playwright.page import PageMethod


# run command: scrapy crawl playwright_handling_headers_demo
class PlaywrightHandlingHeadersDemo(scrapy.Spider):
    """
       Control how requests headers are handled via the PLAYWRIGHT_PROCESS_REQUEST_HEADERS setting.
       If PLAYWRIGHT_PROCESS_REQUEST_HEADERS=None, neither USER_AGENT、cookies will be sent to the
       website
    """
    name = "playwright_handling_headers_demo"

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        # "PLAYWRIGHT_PROCESS_REQUEST_HEADERS": None,
        "USER_AGENT": "Overridden user agent",
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://httpbin.org/headers",
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod(
                        "screenshot", path=Path(__file__).parent / "headers.png", full_page=True
                    ),
                ],
            },
            cookies={"foo": "bar"},
        )

    def parse(self, response):
        headers = json.loads(response.css("pre::text").get())["headers"]
        yield {"url": response.url, "headers": headers}
