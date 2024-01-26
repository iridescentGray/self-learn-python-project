import asyncio
from playwright.async_api import async_playwright


"""
playwright-doc:
https://playwright.dev/python/docs/events
https://playwright.dev/python/docs/dialogs

"""


"""
common_expect_request
"""


async def common_expect_request():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        async with page.expect_request("**/*logo*.png") as first:
            async with page.expect_response("**/*wikipedia.ico") as response_info:
                await page.goto("https://wikipedia.org")
                await page.get_by_label("Search Wikipedia").fill("hello")
                await page.get_by_role("button", name="Search").click()

        await browser.close()


asyncio.run(common_expect_request())

"""
test add/remove listener
"""


def print_request_sent(request):
    print(f"Request sent: {request.url}")


def print_request_finished(request):
    print(f"Request finished:  {request.url}")


def print_response(response):
    print(f"response : {response.status}  {response.url}")


async def request_event():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        page.on("request", print_request_sent)
        page.on("requestfinished", print_request_finished)
        page.on("response", print_response)

        await page.goto("https://wikipedia.org")
        await page.wait_for_timeout(5000)

        # remove
        page.remove_listener("requestfinished", print_request_finished)
        await page.goto("https://www.google.com/")
        await page.wait_for_timeout(5000)

        await browser.close()


asyncio.run(request_event())

"""
test add once listener
"""


async def once_event_listener():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        page.on("dialog", lambda dialog: print(dialog.message))

        await page.goto("https://wikipedia.org")
        await page.wait_for_timeout(1000)

        await page.evaluate("prompt('Enter a number:')")
        # accept 自动输入信息2021 到prompt弹窗
        page.once("dialog", lambda dialog: dialog.accept("2021"))
        await browser.close()


asyncio.run(once_event_listener())
