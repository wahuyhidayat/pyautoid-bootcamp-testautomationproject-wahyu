from selenium.webdriver.common.by import By

class LoginLocators:
    email_input = (By.ID, "inputEmail")
    password_input = (By.ID, "inputPassword")
    login_button = (By.ID, "btnLogin")
    user_account_menu = (By.ID, "user-menu")
    logout_link = (By.LINK_TEXT, "Sign out")
    invalid_login_msg = (By.CSS_SELECTOR, "div.form-control-feedback")
