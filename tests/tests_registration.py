from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers


def test_successful_registration_logged_in_to_account(driver):
    email = helpers.email_generation(4)
    password = helpers.password_generation(8)
    helpers.click_on_log_in_account_button(driver)
    helpers.click_on_word_register(driver)
    helpers.entering_data_for_registration(driver, email, password)
    helpers.click_on_register_button(driver)
    assert driver.find_element(By.XPATH, '//h2[contains(text(),"Вход")]').text == "Вход"


def test_successful_registration_incorrect_password_error(driver):
    email = helpers.email_generation(4)
    password = helpers.password_generation(5)
    helpers.click_on_log_in_account_button(driver)
    helpers.click_on_word_register(driver)
    helpers.entering_data_for_registration(driver, email, password)
    driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
    assert 'Некорректный пароль' == WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//p[contains(text(),"Некорректный пароль")]'))).text


