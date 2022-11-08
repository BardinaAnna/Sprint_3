from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers


def test_transfer_to_personal_account_opens_personal_account_page(authorization):
    helpers.click_on_header_personal_account(authorization)

    assert WebDriverWait(authorization, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
