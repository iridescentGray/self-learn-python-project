# Scrapy settings for scrapy_playwright_demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import playwright
import scrapy

from playwright.async_api import Request
BOT_NAME = "scrapy_playwright_demo"

SPIDER_MODULES = ["scrapy_playwright_demo.spiders"]
NEWSPIDER_MODULE = "scrapy_playwright_demo.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrapy_playwright_demo.middlewares.ScrapyPlaywrightDemoSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "scrapy_playwright_demo.middlewares.ScrapyPlaywrightDemoDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "scrapy_playwright_demo.pipelines.ScrapyPlaywrightDemoPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# -------------------------------------playwright Supported settings--------------------------------------

# The browser type to be launched, e.g. chromium, firefox, webkit.
PLAYWRIGHT_BROWSER_TYPE = "chromium"

# Type dict, default {} ,details: https://github.com/scrapy-plugins/scrapy-playwright#playwright_launch_options
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": False,
    "timeout": 30 * 1000,  # 30 seconds
    # proxy are supported at the Browser level by specifying the proxy key in the PLAYWRIGHT_LAUNCH_OPTIONS setting:
    # "proxy": {
    #     "server": "http://myproxy.com:3128",
    #     "username": "user",
    #     "password": "pass",
    # },
}

# proxy can also be set at the context level with the PLAYWRIGHT_CONTEXTS setting:
# PLAYWRIGHT_CONTEXTS = {
#     "default": {
#         "proxy": {
#             "server": "http://default-proxy.com:3128",
#             "username": "user1",
#             "password": "pass1",
#         },
#     },
#     "alternative": {
#         "proxy": {
#             "server": "http://alternative-proxy.com:3128",
#             "username": "user2",
#             "password": "pass2",
#         },
#     },
# }

# Type dict[str, dict], default {},Define browser contexts variable to start when starting

# PLAYWRIGHT_CONTEXTS = {
#     "foobar": {
#         "context_arg1": "value",
#         "context_arg2": "value",
#     },
#     "default": {
#         "context_arg1": "value",
#         "context_arg2": "value",
#     },
#     "persistent": {
#         "user_data_dir": "/path/to/dir",  # will be a persistent context
#         "context_arg1": "value",
#     },
# }
# Creating a context during a crawl:
# If the context specified in the playwright_context meta key does not exist, it will be created
# You can specify keyword arguments to be passed to Browser.new_context in the playwright_context_kwargs meta key:



# Type Optional[int], default None，Maximum concurrent Playwright limit，unset or None meas no limit
PLAYWRIGHT_MAX_CONTEXTS = 8
# Type Optional[float], default None
# Timeout for Playwright requesting pages，unset or None meas will use default value 30000
PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30 * 1000  # 30 seconds


def custom_headers(
        browser_type: str,
        playwright_request: playwright.async_api.Request,
        scrapy_headers: scrapy.http.headers.Headers,
) -> dict:
    if browser_type == "firefox":
        return {"User-Agent": "foo"}
    return {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}


# Type Optional[Union[Callable, str]]
# default scrapy_playwright.headers.use_scrapy_headers,if unset or None, headers from Scrapy requests will be ignored
# A function that processes headers for every request and return a headers dictionary to be used
# support Coroutine functions
# PLAYWRIGHT_PROCESS_REQUEST_HEADERS = custom_headers

# Type int, defaults  value is Scrapy's CONCURRENT_REQUESTS setting
# Maximum concurrent Playwright pages for each context
PLAYWRIGHT_MAX_PAGES_PER_CONTEXT = 4


# param is playwright.async_api.Request
# def should_abort_request(request):
#     return (
#             request.resource_type == "image" or ".file_type" in request.url
#     )


# Type Optional[Union[Callable, str]], default None
# A predicate function that, return True will aborted request
# aborted requests will not appear in the DEBUG level logs
# PLAYWRIGHT_ABORT_REQUEST = should_abort_request
