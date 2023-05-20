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
        "PLAYWRIGHT_MAX_CONTEXTS": 6,
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
        # using existing contexts
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
        # create a new context
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
        # default context
        yield Request(
            url="https://example.org",
            meta={"playwright": True, "playwright_include_page": True},
            dont_filter=True,
        )
        # each request on a different context
        for i in range(20):
            yield Request(
                url=f"https://example.org?foo={i}",
                meta={
                    "playwright": True,
                    "playwright_context": f"context-{i}",
                    "playwright_include_page": True,
                },
                dont_filter=True,
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        context_name = response.meta["playwright_context"]
        storage_state = await page.context.storage_state()
        await page.context.close()
        return {
            "url": response.url,
            "context": context_name,
            "cookies": storage_state["cookies"],
        }
