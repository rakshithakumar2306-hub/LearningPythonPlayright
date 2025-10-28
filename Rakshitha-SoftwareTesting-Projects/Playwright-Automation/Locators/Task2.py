import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    #age.goto("https://www.w3schools.com/html/html_forms.asp", timeout=60000)
    page.goto("https://www.w3schools.com/html/html_forms.asp", wait_until="domcontentloaded")

    # First Name
    x = page.get_by_label("First name:")
    x.highlight()
    x.fill("Rakshita")

    # Last Name
    y = page.get_by_label("Last name:")
    y.highlight()
    y.fill("K")

    # Screenshot
    page.screenshot(path="./Task2.png")

    browser.close()
