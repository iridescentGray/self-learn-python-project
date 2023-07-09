import asyncio

from playwright.async_api import async_playwright

# load existing authenticated state.
# detail see https://playwright.dev/python/docs/auth

async def login_and_save_status(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto('https://github.com/login')
    # Interact with login form
    await page.get_by_label("Username or email address").fill("Username")
    await page.get_by_label("Password").fill("Password")
    await page.get_by_role("button", name="Sign in").click()
    # Save storage state into the file.
    await context.storage_state(path="state.json")


async def load_login_status(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    # Create a new context with the saved storage state.
    context = await browser.new_context(storage_state="state.json")
    page = await context.new_page()
    await page.goto('https://github.com')
    await asyncio.sleep(10000)
    await browser.close()


async def login_and_save_status_main():
    async with async_playwright() as playwright:
        await login_and_save_status(playwright)


async def load_login_status_main():
    async with async_playwright() as playwright:
        await load_login_status(playwright)


if __name__ == '__main__':
    asyncio.run(login_and_save_status_main())
    # asyncio.run(load_login_status_main())
