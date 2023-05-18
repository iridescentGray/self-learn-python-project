import scrapy


# run command: scrapy crawl playwright_handling_page_events -o result.json
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
                "playwright_page_event_handlers": {
                    "response": "handle_response",
                },
            },
        )

    async def handle_response(self, response) -> None:
        """
        Event handlers will process Playwright objects, not Scrapy.
        such as this function param 'response', it really type is  <class 'playwright.async_api._generated.Response'>
        so we can't use requests/responses as  Scrapy Native Object.
        """
        print(f"Received response with URL {response.url}, {type(response)}")

    def parse(self, response, **kwargs):
        yield None
