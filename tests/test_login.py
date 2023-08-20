import pytest
from selenium import webdriver
from pages.main_page import MainPage


def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login_with_google(browser):
    main_page = MainPage(browser)
    main_page.login_with_google.click()


def test_login_with_facebook(browser):
    main_page = MainPage(browser)
    main_page.login_with_facebook.click()
