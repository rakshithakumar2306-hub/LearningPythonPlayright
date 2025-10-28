import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")

    x=page.get_by_placeholder("What needs to be done?")
    x.fill("Write Playwright tests")
    x.fill("Learn CSS locators")
    x.fill("Practice automation")

    y=page.get_by_text("Learn CSS locators", exact=True)
    y.highlight()
    page.screenshot(path="./Task5.png")

    browser.close()
