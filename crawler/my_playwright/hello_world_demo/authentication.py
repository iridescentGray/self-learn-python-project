import asyncio
import enum
import os

from playwright.async_api import async_playwright, BrowserContext


# load existing authenticated state.
# detail see https://playwright.dev/python/docs/auth


class LoadContextChannel(enum.Enum):
    """
    加载Context的渠道
    """

    # 新建
    NEW = 0
    # 从文件加载
    FROM_FILE = 1


async def run_with_context(func, load_context_channel: LoadContextChannel,
                           context_file_path: str = None) -> None:
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False)
        context = None
        if LoadContextChannel.NEW == load_context_channel:
            context = await browser.new_context()
        if LoadContextChannel.FROM_FILE == load_context_channel:
            if not os.path.exists(context_file_path):
                context = await browser.new_context()
            else:
                context = await browser.new_context(storage_state=context_file_path)
        await func(context)


async def login_and_save_status(browser_context: BrowserContext):
    page = await browser_context.new_page()
    await page.goto('https://github.com/login')
    # Interact with login form
    await page.get_by_label("Username or email address").fill("Username")
    await page.get_by_label("Password").fill("Password")
    await page.get_by_role("button", name="Sign in").click()
    # Save storage state into the file.
    await browser_context.storage_state(path="state.json")


async def load_login_status(browser_context: BrowserContext):
    """看看登陆态的效果"""
    page = await browser_context.new_page()
    await page.goto('https://github.com')
    await asyncio.sleep(10000)


async def is_login(page) -> bool:
    await page.goto('https://github.com/login')
    try:
        # 有登录态时，会跳转到首页
        await page.wait_for_url(url="https://github.com/", timeout=4.0)
        return True
    except Exception:
        return False


async def ensure_login(browser_context) -> None:
    page = await browser_context.new_page()
    is_login_bool = await is_login(page)
    await page.close()
    if not is_login_bool:
        await login_and_save_status(browser_context)


if __name__ == '__main__':
    # ensure_login = run_with_context(func=ensure_login,
    #                                  load_context_channel=LoadContextChannel.FROM_FILE,
    #                                  context_file_path="state.json")
    # asyncio.run(ensure_login)
    load_login_status_test = run_with_context(func=load_login_status,
                                              load_context_channel=LoadContextChannel.FROM_FILE,
                                              context_file_path="state.json")
    asyncio.run(load_login_status_test)
