import scrapy
from scrapy_playwright.page import PageMethod

# run command: scrapy crawl scroll_and_shot_all_screen
class ScrollSpider(scrapy.Spider):
    """
    scroll and then shot_all_screen
    """
    name = "scroll_and_shot_all_screen"
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_DELAY": 3,
        "COOKIES_ENABLED": False,
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "DOWNLOAD_HANDLERS": {
            # "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": False,
            "timeout": 10 * 1000,  # 10 seconds
        },
    }

    def start_requests(self):
        yield scrapy.Request(
            url="http://quotes.toscrape.com/scroll",
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod("wait_for_selector", "div.quote"),
                    PageMethod(
                        "evaluate", "window.scrollBy(0, document.body.scrollHeight)"
                    ),
                    PageMethod(
                        "wait_for_selector", "div.quote:nth-child(11)"
                    ),  # 10 per page
                ],
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.screenshot(path="quotes.png", full_page=True)
        await page.close()
        return {
            "quote_count": len(response.css("div.quote"))
        }  # quotes from several pages
