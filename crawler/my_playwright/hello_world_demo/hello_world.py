import re

import pytest
from playwright.sync_api import Page, expect


# The Playwright Pytest plugin is based on the concept of test fixtures such as the built in page fixture,
# which is passed into your test as the param :'page: Page'
# Pages are isolated between tests due to the Browser Context, which is equivalent to a brand new browser profile,
# where every test gets a fresh environment, even when multiple tests run in a single Browser.
def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    # expect function which will wait until the expected condition is met.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    # Locators are the central piece of Playwright's auto-waiting and retry-ability.
    # it is a way to find element(s) on the page and perform actions on elements such as .click .fill
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))


# You can use various fixtures to execute code before or after your tests and to share objects between them.
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url before each test.
    print("executeTask")
    yield
    print("afterEach")
