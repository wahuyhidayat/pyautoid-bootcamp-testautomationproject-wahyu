import pytest
from Locators.locators import LoginLocators
from Pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize('email, password', [
        ("user@gmail.com", "wrongPassword"),
        ("why.hidayat98@gmail.com", "wrongPassword"),
        ("user@gmail.com", "qasef0rq4")
    ])
    def test_login_failed(self, email, password):
        loginPage = LoginPage(self.driver)
        loginPage.set_user_inputs(email, password)
        error_msg = self.driver.find_element(*LoginLocators.invalid_login_msg).text
        assert error_msg == "These credentials do not match our records."

    def test_login_passed(self):
        loginPage = LoginPage(self.driver)
        loginPage.set_user_inputs("why.hidayat98@gmail.com", "qasef0rq4")
        dashboard_title = self.driver.title
        assert dashboard_title == "Projects | Qase"
        loginPage.expand_account_menu()
        loginPage.logout()
