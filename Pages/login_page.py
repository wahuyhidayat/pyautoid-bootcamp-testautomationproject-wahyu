from Locators.locators import LoginLocators


class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://app.qase.io/login")

    def set_user_inputs(self, email, password):
        self.driver.find_element(*LoginLocators.email_input).send_keys(email)
        self.driver.find_element(*LoginLocators.password_input).send_keys(password)
        self.driver.find_element(*LoginLocators.login_button).click()

    def expand_account_menu(self):
        self.driver.find_element(*LoginLocators.user_account_menu).click()

    def logout(self):
        self.driver.find_element(*LoginLocators.logout_link).click()
