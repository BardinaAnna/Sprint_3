from selenium.webdriver.common.by import By
import helpers


def test_go_to_sauces_section_with_rolls_display_sauces(driver):
    helpers.click_sauce(driver)
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text == "Соусы"


def test_go_to_sauces_section_with_fillings_display_sauces(driver):
    helpers.click_filling(driver)
    helpers.click_sauce(driver)
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text == "Соусы"


def test_go_to_fillings_section_with_rolls_display_fillings(driver):
    helpers.click_filling(driver)
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").text == "Начинки"


def test_go_to_fillings_section_with_sauces_display_fillings(driver):
    helpers.click_sauce(driver)
    helpers.click_filling(driver)
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").text == "Начинки"


def test_go_to_rolls_section_with_sauces_display_rolls(driver):
    helpers.click_sauce(driver)
    helpers.click_rolls(driver)
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text == "Булки"


def test_go_to_rolls_section_with_fillings_display_rolls(driver):
    helpers.click_filling(driver)
    helpers.click_rolls(driver)
    assert driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text == "Булки"
