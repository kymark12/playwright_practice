from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.get_username_label = self.page.get_by_label("Username")
        self.username_field = self.page.locator("input[id='username']")
        self.password_field = self.page.locator("input[id='password']")
        self.terms_and_condition = self.page.locator("input[id='terms']")
        self.sign_in_button = self.page.locator("input[id='signInBtn']")

    def go_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        expect(self.get_username_label).to_be_visible()

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.terms_and_condition.click()
        self.sign_in_button.click()

