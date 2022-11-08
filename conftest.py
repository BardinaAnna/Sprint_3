import pytest
import helpers
import random
import names
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    yield driver

    driver.quit()

@pytest.fixture()
def password():
    chars  = '+-/*!&$#=@<>.,qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    password = ''
    for i in range(8):
        password += random.choice(chars)
    return password

@pytest.fixture()
def email():
    numbers = '1234567890'
    email = names.names[random.randint(0,len(names.names))]
    email += str(4)
    for i in range(3):
        email += random.choice(numbers)
    email += '@yandex.ru'
    return email


@pytest.fixture()
def registration(driver, email, password):
    helpers.click_on_log_in_account_button(driver)
    helpers.click_on_word_register(driver)
    helpers.entering_data_for_registration(driver, email, password)
    helpers.click_on_register_button(driver)
    return driver

@pytest.fixture()
def authorization(registration, email, password):
    helpers.entering_data_log_in_to_account(registration, email, password)
    helpers.click_on_login_button(registration)
    return registration

@pytest.fixture()
def profile(authorization):
    helpers.click_on_header_personal_account(authorization)
    return authorization