from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import random

async def launch_stealth(proxy: str | None = None):
    p = await async_playwright().start()
    browser = await p.chromium.launch(
        headless=True,
        proxy={'server': proxy} if proxy else None
    )
    context = await browser.new_context(
        locale=random.choice(["en-US", "fr-FR", "de-DE", "en-GB"]),
        geolocation={"longitude": 36.8, "latitude": -1.3},
        permissions=["geolocation"]
    )
    page = await context.new_page()
    await stealth_async(page)
    await page.add_init_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return p, browser, page
