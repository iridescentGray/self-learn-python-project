import asyncio

from playwright.async_api import async_playwright

"""
playwright-doc:
https://playwright.dev/python/docs/emulation
"""


"""
select devices

all-support-devices:
https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json

"""


async def select_devices():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        iphone = playwright.devices["iPhone 13"]
        browser = await chromium.launch(headless=False)
        context = await browser.new_context(**iphone)
        page = await context.new_page()
        await page.goto("https://www.google.com")
        await browser.close()


asyncio.run(select_devices())


"""
is_mobile

"""


async def change_viewport():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1280, "height": 1024})
        page = await context.new_page()
        await page.goto("https://www.google.com")
        await page.set_viewport_size({"width": 1600, "height": 1200})
        await browser.close()


asyncio.run(change_viewport())

"""
is_mobile
"""


async def is_mobile():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context(is_mobile=True)
        page = await context.new_page()
        await page.goto("https://www.google.com")
        await browser.close()


asyncio.run(is_mobile())


"""
Locale & Timezone
"""


async def locale_timezone():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context(
            locale="de-DE",
            timezone_id="Europe/Berlin",
        )
        page = await context.new_page()
        await page.goto("https://www.google.com")
        await browser.close()


asyncio.run(locale_timezone())

"""
geolocation
"""


async def geolocation():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context(
            geolocation={"longitude": 41.890221, "latitude": 12.492348},
            permissions=["geolocation"],
        )
        page = await context.new_page()
        await page.goto("https://www.google.com/maps")
        await browser.close()


asyncio.run(geolocation())


"""
javascript
"""


async def javascript():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = await browser.new_context(java_script_enabled=False)
        page = await context.new_page()
        await page.goto("https://www.bilibili.com/")
        await browser.close()


asyncio.run(javascript())
