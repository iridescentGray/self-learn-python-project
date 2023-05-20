import scrapy
from scrapy import Spider


# run command: scrapy crawl supported_request_meta_keys_demo
class SupportedRequestMetaKeysDemo(Spider):
    name = "supported_request_meta_keys_demo"
    """
        this class is used to demo  <Request.meta>  keys for playwright.
        <Request.meta> is A dict that contains arbitrary metadata for this request.This dict is empty for new Requests,
        and is usually populated by different Scrapy components (extensions, middlewares, etc).
        So the data contained in this dict depends on the extensions you have enabled.
        source doc: https://docs.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request.meta
    """

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
    }

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

                # Type Optional[playwright.async_api.Page], default None
                #  If unspecified, a new page is created for each request.
                #  This key could be used in conjunction with 'playwright_include_page=True' to make a chain of requests using the same page
                "playwright_page": None,

                # Type Dict[Str, Callable], default {},
                # A dictionary of handlers to be attached to page events
                # Keys are the name of the event to be handled
                # Values can be either actual callables or spider member method name str
                # Examples are as follows:
                # playwright_handling_page_events.py
                # https://github.com/scrapy-plugins/scrapy-playwright#handling-page-events
                "playwright_page_event_handlers": {
                },

                # Type Optional[Union[Callable, str]], default None
                # A coroutine function to be invoked immediately after creating a page for the request.
                # It receives the page and the request as positional arguments.
                # Useful for initialization code. Invoked only for newly created pages.
                # Code Examples are as follows:
                # playwright_page_init_callback_demo.py
                "playwright_page_init_callback": None,

                # Type Iterable[PageMethod], default (),require A sorted iterable of PageMethod
                # PageMethod invoke before returning the final response.
                # PageMethod is useful when need to perform certain actions on a page(such scrolling down or clicking links)
                # All Method Playwright Support,see follow doc:
                # https://playwright.dev/python/docs/api/class-page
                # Code Examples are as follows:
                # playwright_page_method_demo.py
                "playwright_page_methods": None,

                # Type dict, default {}
                # A dictionary with keyword arguments to be passed to the page's goto method when navigating to an URL.
                # Examples are as follows:
                # https://playwright.dev/python/docs/api/class-page#page-goto
                "playwright_page_goto_kwargs": {
                    "wait_until": "networkidle",
                },

                # playwright_security_details
                # Type Optional[dict], read only,can't change
                # A dictionary with security information about the give response.
                # Only available for HTTPS requests.
                # you can get it from  response.meta
                # print(response.meta["playwright_security_details"])

            },
        )

    def parse(self, response):
        yield {"url": response.url}
