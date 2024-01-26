import asyncio
from pathlib import Path
from playwright.async_api import async_playwright, expect

"""
playwright-doc:
https://playwright.dev/python/docs/mock#mocking-with-har-files
"""


async def save_har():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.route_from_har(
            har=Path.cwd() / "fruit.har", url="*/**/api/v1/fruits", update=True
        )
        await page.goto("https://demo.playwright.dev/api-mocking")

        await expect(page.get_by_text("Strawberry", exact=True)).to_be_visible()

        # close is necessary
        await page.close()
        await context.close()
        await browser.close()


asyncio.run(save_har())


async def replaying_from_har():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.route_from_har(
            Path.cwd() / "fruit.har", url="*/**/api/v1/fruits", update=False
        )
        await page.goto("https://demo.playwright.dev/api-mocking")

        await expect(page.get_by_text("Strawberry")).to_be_visible()

        await page.close()
        await context.close()
        await browser.close()


asyncio.run(replaying_from_har())
