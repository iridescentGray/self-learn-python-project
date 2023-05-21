from pathlib import Path

import scrapy
from scrapy import Request


# run command: scrapy crawl playwright_multiple_contexts_demo
class PlaywrightMultipleContextsDemo(scrapy.Spider):
    """
    Handle multiple browser contexts
    """

    name = "playwright_multiple_contexts_demo"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "CONCURRENT_REQUESTS": 16,
        "PLAYWRIGHT_MAX_CONTEXTS": 4,
        "FEEDS": {
            "playwright_multiple_contexts_demo.json": {"format": "json", "encoding": "utf-8", "indent": 4},
        },
        "PLAYWRIGHT_CONTEXTS": {
            "first": {
                "storage_state": {
                    "cookies": [
                        {
                            "url": "https://example.org",
                            "name": "context",
                            "value": "first",
                        },
                    ],
                },
            },
            "second": {
                "storage_state": {
                    "cookies": [
                        {
                            "url": "https://example.org",
                            "name": "context",
                            "value": "second",
                        },
                    ],
                },
            },
            "persistent": {
                "user_data_dir": str(Path.home() / "playwright-persistent-context"),
                "java_script_enabled": False,
            },
        },
    }

    def start_requests(self):
        # 1. using existing contexts (first,second)
        for ctx_name in self.custom_settings["PLAYWRIGHT_CONTEXTS"].keys():
            yield Request(
                url="https://example.org",
                meta={
                    "playwright": True,
                    "playwright_context": ctx_name,
                    "playwright_include_page": True,
                },
                dont_filter=True,
            )
        # 2.create a new context named 'third',it will override old value
        yield Request(
            url="https://example.org",
            meta={
                "playwright": True,
                "playwright_context": "third",
                "playwright_context_kwargs": {
                    "storage_state": {
                        "cookies": [
                            {
                                "url": "https://example.org",
                                "name": "context",
                                "value": "third",
                            },
                        ],
                    },
                },
                "playwright_include_page": True,
            },
            dont_filter=True,
        )
        # 3.default context
        yield Request(
            url="https://example.org",
            meta={"playwright": True, "playwright_include_page": True},
            dont_filter=True,
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        # get context
        context_name = response.meta["playwright_context"]
        # get value from context
        storage_state = await page.context.storage_state()
        await page.context.close()
        return {
            "url": response.url,
            "context": context_name,
            "cookies": storage_state["cookies"],
        }

    async def errback_close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
