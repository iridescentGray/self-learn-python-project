import asyncio

from playwright.async_api import async_playwright

"""
playwright-doc:
https://playwright.dev/python/docs/frames
https://playwright.dev/python/docs/api/class-frame
https://playwright.dev/python/docs/api/class-framelocator
"""


async def main():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False, slow_mo=1000)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://store.steampowered.com/join")
        frame = page.frame_locator('iframe[title="reCAPTCHA"]')
        await frame.get_by_role("checkbox").click()

        await browser.close()


asyncio.run(main())
