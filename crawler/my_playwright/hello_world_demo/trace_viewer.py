import asyncio

from playwright.async_api import async_playwright

"""
playwright-doc:
https://playwright.dev/python/docs/trace-viewer-intro
https://playwright.dev/python/docs/trace-viewer

web-trace-view:
https://trace.playwright.dev/
"""


async def run_main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            headless=False
        )  # or "firefox" or "webkit".
        context = await browser.new_context()

        # Start tracing before creating / navigating a page.
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = await context.new_page()
        await page.goto("https://playwright.dev")

        # Stop tracing and export it into a zip archive.
        await context.tracing.stop(path="trace.zip")


asyncio.run(run_main())


# run commond to view trace
import subprocess

command = "playwright show-trace trace.zip"
result = subprocess.run(command, shell=True, check=True, text=True)
