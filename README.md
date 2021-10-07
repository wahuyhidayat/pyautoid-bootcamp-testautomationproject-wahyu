# Test Automation Project
This is my first test automation project based on Selenium-Webdriver with Python. The test contains user login tests (correct/incorrect email and password)

# Project Structure
Here you can find a short description of the main directories and it's content
- [Locators](https://github.com/wahuyhidayat/pyautoid-bootcamp-testautomationproject-wahyu/tree/main/Locators): there are locators of web elements
- [Pages](https://github.com/wahuyhidayat/pyautoid-bootcamp-testautomationproject-wahyu/tree/main/Pages): there are sets of methods for each test
- [Tests](https://github.com/wahuyhidayat/pyautoid-bootcamp-testautomationproject-wahyu/tree/main/Tests): there are sets of tests for the main functionalities of the website
- [Reports](https://github.com/wahuyhidayat/pyautoid-bootcamp-testautomationproject-wahyu/tree/main/Reports): if you run tests with pytest-html, tests reports will be saved in this directory

# Getting Started
To enjoy the automated tests, develop the framework or adapt it to your own purpose, just download the project or clone repository.

# Run Automated Tests
To run the selected test without pytest-html, you can run the test in command prompt by using this command:
```bash
pytest -v Tests/test_login.py
```

# Generate Test Report
To generate all tests report using pytest-html you can run tests by using this command:
```bash
pytest -v Tests/test_login.py --html=Reports/report-name.html
```
