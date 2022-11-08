from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers

def test_transfer_from_personal_accaunt_to_constructor_by_clicking_constructor_header_transfer_constructor(profile):
    helpers.click_on_header_сonstructor(profile)
    assert WebDriverWait(profile, 3).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))).text == "Соберите бургер"


def test_transfer_from_personal_accaunt_to_constructor_by_clicking_logo_transfer_constructor(profile):
    helpers.click_on_header_logo(profile)
    assert WebDriverWait(profile, 3).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))).text == "Соберите бургер"
