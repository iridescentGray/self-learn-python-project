import scrapy
from scrapy_playwright.page import PageMethod


# run command: scrapy crawl click_and_save_the_resulting_as_pdf
class ClickAndSaveTheResultingAsPdf(scrapy.Spider):
    name = "click_and_save_the_resulting_as_pdf"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": False,
            "timeout": 10 * 1000,  # 10 seconds
        },
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://example.org",
            meta=dict(
                playwright=True,
                playwright_page_methods={
                    "click": PageMethod("click", selector="a"),
                    "pdf": PageMethod("pdf", path="./file.pdf"),
                },
            ),
        )

    def parse(self, response):
        pdf_bytes = response.meta["playwright_page_methods"]["pdf"].result
        with open("iana.pdf", "wb") as fp:
            fp.write(pdf_bytes)
        # response.url is "https://www.iana.org/domains/reserved"
        yield {"url": response.url}
