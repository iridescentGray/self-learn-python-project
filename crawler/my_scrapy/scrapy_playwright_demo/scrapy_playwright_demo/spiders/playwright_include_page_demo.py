import scrapy


# run command: scrapy crawl playwright_include_page_demo -o result.json
class PlaywrightIncludePageDemo(scrapy.Spider):
    name = "playwright_include_page_demo"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },

    }
    def start_requests(self):
        yield scrapy.Request(url="https://example.org",
                             callback=self.parse,
                             dont_filter=True)

    def parse(self, response, **kwargs):
        yield scrapy.Request(
            url="https://example.org",
            callback=self.parse_next,
            meta={"playwright": True,
                  "playwright_include_page": True},
            errback=self.errback_close_page,
        )

    async def parse_next(self, response, **kwargs):
        page = response.meta["playwright_page"]
        title = await page.title()  # "Example Domain"
        await page.close()
        return {"title": title}

    async def errback_close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
