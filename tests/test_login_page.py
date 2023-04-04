from playwright.sync_api import Playwright
from pom.login import LoginPage

"""
Scenario:
1. Login using username and password
2. Agree to the terms and conditions
3. Click Sign In button
"""


def test_login_successfully(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    login_page = LoginPage(page)
    login_page.go_to_login_page()
    login_page.login(username="rahulshettyacademy",
                     password="learning")


# with sync_playwright() as playwright:
#     test_login_successfully(playwright)
