import logging

from scrapy import Request
from scrapy import Spider


# run command: scrapy crawl handle_exception_errback_demo
class HandleExceptionInErrbackSpider(Spider):
    """
    Handle exceptions in the Playwright downloader, such as TimeoutError
    """

    name = "handle_exception_errback_demo"
    custom_settings = {
        "PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT": 3000,  # milliseconds
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "RETRY_TIMES": 3,
    }

    def start_requests(self):
        yield Request(
            # delay 10 seconds
            url="https://httpbin.org/delay/10",
            meta={"playwright": True, "playwright_include_page": True},
            errback=self.errback,
        )

    async def errback(self, failure):
        logging.info(
            "Handling failure in errback, request=%r, exception=%r", failure.request, failure.value
        )
        # you can tru to reload the page
        # page = failure.request.meta["playwright_page"]
        # await page.reload()
