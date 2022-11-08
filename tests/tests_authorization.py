from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers


def test_authorization_by_clicking_Log_in_to_account_home_page(registration, email, password):
    registration.get('https://stellarburgers.nomoreparties.site/')
    helpers.click_on_log_in_account_button(registration)
    helpers.entering_data_log_in_to_account(registration, email, password)
    helpers.click_on_login_button(registration)

    assert registration.find_element(By.XPATH, ".//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"


def test_authorization_through_Personal_Account_button(registration, email, password):
    registration.get('https://stellarburgers.nomoreparties.site/')
    helpers.click_on_header_personal_account(registration)
    WebDriverWait(registration, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Вход")]')))
    helpers.entering_data_log_in_to_account(registration, email, password)
    helpers.click_on_login_button(registration)

    assert registration.find_element(By.XPATH, ".//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"


def test_authorization_button_in_registration_form(registration, email, password):
    registration.get('https://stellarburgers.nomoreparties.site/')
    helpers.click_on_log_in_account_button(registration)
    helpers.click_on_word_register(registration)
    helpers.click_on_word_log_in(registration)
    helpers.entering_data_log_in_to_account(registration, email, password)
    helpers.click_on_login_button(registration)

    assert registration.find_element(By.XPATH, ".//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"


def test_authorization_button_in_password_recovery_form(registration, email, password):
    registration.get('https://stellarburgers.nomoreparties.site/')
    helpers.click_on_log_in_account_button(registration)
    helpers.click_on_password_recovery_button(registration)
    helpers.click_on_word_log_in(registration)
    helpers.entering_data_log_in_to_account(registration, email, password)
    helpers.click_on_login_button(registration)

    assert registration.find_element(By.XPATH, ".//button[contains(text(),'Оформить заказ')]").text == "Оформить заказ"