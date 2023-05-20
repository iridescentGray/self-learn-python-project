import scrapy
from playwright.async_api import Dialog, Response as PlaywrightResponse
from scrapy_playwright.page import PageMethod


# run command: scrapy crawl playwright_handling_page_events
class PlaywrightHandlingPageEvents(scrapy.Spider):
    name = "playwright_handling_page_events"

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },

    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://example.org",
            callback=self.parse,
            meta={
                "playwright": True,
                # Event handlers will remain attached to the page
                # Fortunately,This is usually not a problem, page are single-use.
                "playwright_page_methods": [
                    PageMethod("evaluate", "alert('foobar');"),
                ],
                "playwright_page_event_handlers": {
                    "dialog": self.handle_dialog,
                    "response": "handle_response",
                },
            },
        )

    async def handle_dialog(self, dialog: Dialog) -> None:
        print(f"Handled dialog with message: {dialog.message}")
        await dialog.dismiss()

    async def handle_response(self, response: PlaywrightResponse) -> None:
        """
        Event handlers will process Playwright objects, not Scrapy.
        such as this function param 'response', it really type is  <class 'playwright.async_api._generated.Response'>
        so we can't use requests/responses as  Scrapy Native Object.
        """
        print(f"Received response with URL {response.url}")

    def parse(self, response, **kwargs):
        return {"url": response.url}
