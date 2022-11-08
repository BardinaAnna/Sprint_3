from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers

def test_log_out_log_out(profile):
    helpers.click_on_exit_button(profile)

    assert WebDriverWait(profile, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))
