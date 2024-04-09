import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

"""
playwright-doc:
https://playwright.dev/python/docs/writing-tests
"""


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_records_or_updates_the_har_file(page: Page):
    page.route_from_har(
        har=Path.cwd() / "fruit.har", url="*/**/api/v1/fruits", update=True
    )

    # Go to the page
    page.goto("https://demo.playwright.dev/api-mocking")

    # Assert that the Playwright fruit is visible
    expect(page.get_by_text("Strawberry", exact=True)).to_be_visible()


# You can use various fixtures to execute code before or after your tests and to share objects between them.
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url before each test.
    print("executeTask")
    yield
    print("afterEach")
