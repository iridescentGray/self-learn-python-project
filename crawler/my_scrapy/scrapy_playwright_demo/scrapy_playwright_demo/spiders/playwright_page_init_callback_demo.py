import scrapy


async def init_page(page, request):
    await page.set_extra_http_headers({"Asdf": "Qwerty"})
    print("init_page is execute")
    await page.add_init_script(path="./resource/custom_script.js")


# run command: scrapy crawl playwright_page_init_callback_demo
class PlaywrightIncludePageDemo(scrapy.Spider):
    name = "playwright_page_init_callback_demo"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://httpbin.org/headers",
            meta={
                "playwright": True,
                "playwright_page_init_callback": init_page,
            },
        )

    async def parse(self, response, **kwargs):
        yield None
