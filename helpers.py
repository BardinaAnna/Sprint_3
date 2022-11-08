import random
import names
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def password_generation(linght):
    chars  = '+-/*!&$#=@<>.,qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    password = ''

    for i in range(linght):
        password += random.choice(chars)

    return password


def email_generation(cohort):
    numbers = '1234567890'

    email = names.names[random.randint(0,len(names.names))]
    email += str(cohort)
    for i in range(3):
        email += random.choice(numbers)
    email += '@yandex.ru'

    return email


def entering_data_for_registration(driver, email, password):
    driver.find_element(By.XPATH, "//fieldset[1]//input[@type='text']").send_keys("Anna")       #Поле для ввода имени
    driver.find_element(By.XPATH, "//fieldset[2]//input[@type='text']").send_keys(email)        #Поле для ввода емейла
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)              #Поле для ввода пароля


def click_on_register_button(driver):
    driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()    #Кнопка зарегестрироватся
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Вход")]')))    #Заколовок в форме авторизации


def click_on_log_in_account_button(driver):
    driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()   #Кнопка входа в аккаунт на главной странице
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Вход")]')))


def click_on_word_register(driver):
    driver.find_element(By.XPATH, '//a[contains(text(),"Зарегистрироваться")]').click()   #Ссылка для перехода в форму регистрации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Регистрация")]'))) #Заголовок в формет регистрации


def entering_data_log_in_to_account(driver, email, password):
    driver.find_element(By.XPATH, "//fieldset[1]//input[@type='text']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)


def click_on_login_button(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()     #Кнопка "Войти" в ворме авторизации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//button[contains(text(),'Оформить заказ')]")))  #Кнопка "Оформить заказ" на главной странице


def click_on_header_personal_account(driver):
    driver.find_element(By.XPATH, "//a[@href='/account']").click()   #Хедер "Личный кабинет"


def click_on_word_log_in(driver):
    driver.find_element(By.XPATH, "//a[@href='/login']").click()   #Ссылка "Войти" для перехода на страницу авторизации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Вход")]')))


def click_on_password_recovery_button(driver):
    driver.find_element(By.XPATH, "//a[@href='/forgot-password']").click()   #Ссылка "Восстановление пароля" для перехода на форму восстановление пароля с формы авторизации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")))   #Заголовок в форме восстановления пароля


def click_on_header_сonstructor(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li/a[@href='/']"))).click()      #Хедр "Конструктор"


def click_on_header_logo(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/a[@href='/']"))).click()     #Хедр логитип


def click_on_exit_button(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]"))).click()   #Кнопка выхода из личного кабинета


def click_sauce(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]/..").click()    #Раздел соусы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Соусы')]"))) #Заголовок в разделе соусы


def click_filling(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]/..").click()  #Раздел начинки
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Начинки')]"))) #Заголовок в разделе начинки


def click_rolls(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]/..").click()    #Раздел булки
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))   #Заголовок в разделе булки