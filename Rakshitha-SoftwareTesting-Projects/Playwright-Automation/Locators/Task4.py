import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    #b= page.locator(".btn.btn-primary")
    b = page.get_by_role("button", name="Button", exact=True).nth(2)
    b.highlight()

    if b.is_visible():
        b.click()
    else:
        print("Button not visible")

    page.screenshot(path="./Task4.png")

    browser.close()
