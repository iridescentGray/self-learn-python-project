from pathlib import Path

from scrapy import Spider, FormRequest
from scrapy_playwright.page import PageMethod


# run command: scrapy crawl send_post_request -o result.json
class PostSpider(Spider):
    """
    Send data using the POST
    """

    name = "send_post_request"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            # "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
    }

    def start_requests(self):
        yield FormRequest(
            url="https://httpbin.org/post",
            formdata={"foo": "bar"},
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod(
                        # 给请求截图
                        "screenshot", path=Path(__file__).parent / "send_post_request.png", full_page=True
                    ),
                ],
            },
        )

    def parse(self, response):
        yield {"url": response.url}
