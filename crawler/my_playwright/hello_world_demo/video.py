import asyncio
from playwright.async_api import async_playwright

"""
playwright-doc:
https://playwright.dev/python/docs/videos

"""


async def mock_api_requests():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(record_video_dir="videos/")
        page = await context.new_page()
        await page.goto("https://demo.playwright.dev/api-mocking")
        await page.goto("https://www.google.com/")
        await page.goto("https://translate.google.com")
        print(await page.video.path())
        await browser.close()


asyncio.run(mock_api_requests())
