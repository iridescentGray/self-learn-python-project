from pathlib import Path

import scrapy
from scrapy import Spider
from scrapy_playwright.page import PageMethod


class SupportedRequestMetaKeysDemo(Spider):
    """
        this class is used to demo  <Request.meta>  keys for playwright.
        <Request.meta> is A dict that contains arbitrary metadata for this request.This dict is empty for new Requests,
        and is usually populated by different Scrapy components (extensions, middlewares, etc).
        So the data contained in this dict depends on the extensions you have enabled.
        source doc: https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request.meta
    """

    def start_requests(self):
        yield scrapy.Request(
            url="https://example.org",
            meta={
                # Type bool, default False, if True this request will be processed by Playwright.
                "playwright": True,
                # Type str, default "default" ,Name of the context to be used to download the request
                # relevant doc: https://playwright.dev/python/docs/browser-contexts
                "playwright_context": "awesome_context",
                # Type dict, default {}, dictionary with keyword arguments to be used when creating a new context,
                # if a context with the name specified in the playwright_context meta key does not exist already
                "playwright_context_kwargs": {
                    "ignore_https_errors": True,
                },
                # Type bool, default False,
                # if True, the Playwright page can be available in the callback at response.meta['playwright_page']
                # this option is not necessary, this option Don't influence PageMethod to be applied and page load
                # only if you need access to the Page object in the callback response,Examples are as follows:
                # playwright_include_page_demo.py
                # https://github.com/scrapy-plugins/scrapy-playwright#receiving-page-objects-in-callbacks
                "playwright_include_page": True,

                # Type Dict[Str, Callable], default {},
                # Keys are the name of the event to be handled
                # Values can be either actual callables or spider member method name str
                # Examples are as follows:
                # playwright_handling_page_events.py
                # https://github.com/scrapy-plugins/scrapy-playwright#handling-page-events
                "playwright_page_event_handlers": {
                },
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
