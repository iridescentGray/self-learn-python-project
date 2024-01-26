import asyncio
from playwright.async_api import async_playwright, Playwright

"""
playwright-doc:
https://playwright.dev/python/docs/extensibility
https://playwright.dev/python/docs/api/class-selectors
"""


async def run(playwright: Playwright):
    tag_selector = """
      {
          // Returns the first element matching given selector in the root's subtree.
          query(root, selector) {
              return root.querySelector(selector);
          },
          // Returns all elements matching given selector in the root's subtree.
          queryAll(root, selector) {
              return Array.from(root.querySelectorAll(selector));
          }
      }"""

    # Register the engine. Selectors will be prefixed with "tag=".
    await playwright.selectors.register("tag", tag_selector)
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.set_content(
        f"<div><button onclick='console.log(1111111)'>Click me</button></div>"
    )

    button = await page.query_selector("tag=button")
    await button.click()
    await page.locator("tag=div").get_by_text("Click me").click()
    button_count = await page.locator("tag=button").count()
    print(button_count)
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
