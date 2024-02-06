from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        page.screenshot(path=f"example-{browser_type.name}.png")
        print("screenshot success")
        browser.close()
