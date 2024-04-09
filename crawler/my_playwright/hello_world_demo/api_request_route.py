import asyncio

from playwright.async_api import Route, async_playwright, expect

"""
playwright-doc:
https://playwright.dev/python/docs/mock
https://playwright.dev/python/docs/network#handle-requests
"""


async def mock_api_requests():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        async def request_route(route: Route):
            json = [{"name": "Strawberry", "id": 21}]
            await route.fulfill(json=json)

        async def header_route(route):
            headers = route.request.headers
            print(f"----------headers----------------/n {headers}")
            await route.continue_(headers=headers)

        # ohter wait to mock
        # await page.route("*/**/api/v1/fruits", lambda route: ...)
        await page.route("*/**/api/v1/fruits", request_route)
        await page.route("**/*", header_route)
        # abort image
        await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())

        await page.goto("https://demo.playwright.dev/api-mocking")
        await expect(page.get_by_text("Strawberry")).to_be_visible()
        await browser.close()


asyncio.run(mock_api_requests())


async def mock_api_response():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        async def add_response_json(route: Route):
            response = await route.fetch()
            json = await response.json()
            json.append({"name": "Playwright", "id": 100})
            await route.fulfill(response=response, json=json)

        await page.route(
            "https://demo.playwright.dev/api-mocking/api/v1/fruits", add_response_json
        )

        await page.route(
            "https://demo.playwright.dev/api-mocking/api/v1/fruits", add_response_json
        )
        await page.goto("https://demo.playwright.dev/api-mocking")

        await expect(page.get_by_text("Playwright", exact=True)).to_be_visible()
        await browser.close()


asyncio.run(mock_api_response())
