import asyncio
from playwright.async_api import async_playwright, Playwright

REPO = "test-github-repo1"
USER = ""
API_TOKEN = ""

"""
playwright-doc:
https://playwright.dev/python/docs/api-testing

creatae apis tokens
https://github.com/settings/tokens
"""


async def run(playwright: Playwright):
    browser = await playwright.chromium.launch()
    context = await browser.new_context(base_url="https://api.github.com")
    api_request_context = context.request
    page = await context.new_page()
    # Create a repository.
    response = await api_request_context.post(
        # not need prefix
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {API_TOKEN}",
        },
        data={"name": REPO},
    )
    assert response.ok

    # Delete a repository.
    response = await api_request_context.delete(
        f"/repos/{USER}/{REPO}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {API_TOKEN}",
        },
    )
    assert response.ok


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
