import asyncio
import functools
import os
import typing
from contextlib import asynccontextmanager

from playwright.async_api import BrowserContext, async_playwright

"""
playwright-doc:
https://playwright.dev/python/docs/auth
"""

# load existing authenticated state.
# detail see https://playwright.dev/python/docs/auth


def with_playwright_context(
    func: typing.Optional[typing.Callable] = None,
    *,
    load_file_first: bool = True,
    context_file_path: str = "./state.json"
) -> typing.Callable:
    @asynccontextmanager
    async def create_playwright_context(
        *, load_file_first: bool, context_file_path: str
    ) -> typing.AsyncGenerator:
        async with async_playwright() as playwright:
            chromium = playwright.chromium
            browser = await chromium.launch(headless=False)
            if not load_file_first:
                context = await browser.new_context()
            else:
                if not (context_file_path and os.path.exists(context_file_path)):
                    context = await browser.new_context()
                else:
                    context = await browser.new_context(storage_state=context_file_path)
            try:
                yield context
            finally:
                await context.close()
                await browser.close()

    async def is_context_already_exit(*args, **kwargs) -> bool:
        if kwargs.get("browser_context", None):
            return True
        for arg in args:
            if isinstance(arg, BrowserContext):
                return True
        return False

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            if await is_context_already_exit(*args, **kwargs):
                return await func(*args, **kwargs)
            else:
                async with create_playwright_context(
                    load_file_first=load_file_first, context_file_path=context_file_path
                ) as browser_context:
                    kwargs["browser_context"] = browser_context
                    return await func(*args, **kwargs)

        return wrapper

    return decorator


@with_playwright_context()
async def is_login(browser_context: typing.Optional[BrowserContext] = None) -> bool:
    page = await browser_context.new_page()
    await page.goto("https://github.com/")
    logged_in_element = await page.query_selector(".AppHeader-user .avatar")
    is_logged_in = bool(logged_in_element)
    return is_logged_in


@with_playwright_context()
async def login_and_save_status(
    browser_context: typing.Optional[BrowserContext] = None,
):
    page = await browser_context.new_page()
    await page.goto("https://github.com/login")
    # Interact with login form
    await page.get_by_label("Username or email address").fill("")
    await page.get_by_label("Password").fill("")
    await page.get_by_role("button", name="Sign in").click()
    # Save storage state into the file.
    await page.wait_for_url(url="https://github.com/sessions/two-factor/app")

    # 尝试登陆
    for i in range(1, 4):
        code = await get_two_factor()
        await page.get_by_placeholder("XXXXXX").fill(code)
        try:
            await page.wait_for_url(
                url="https://github.com/",
                timeout=2000.0,
                wait_until="domcontentloaded",
            )
            break
        except Exception:
            continue

    await browser_context.storage_state(path="state.json")


async def get_two_factor() -> str:
    return "090959"


@with_playwright_context()
async def ensure_login(browser_context: typing.Optional[BrowserContext] = None) -> None:
    is_login_bool = await is_login(browser_context)
    if not is_login_bool:
        await login_and_save_status(browser_context)


if __name__ == "__main__":
    asyncio.run(ensure_login())
    # asyncio.run(is_login())
    # asyncio.run(login_and_save_status())
