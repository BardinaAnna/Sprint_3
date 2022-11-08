# Sprint_3
# Бардина Анна Сергеевна

tests_registration - Тесты на проверку регистрации 
    test_successful_registration_logged_in_to_account() - Позитивный тест на регистрацию    
    test_successful_registration_incorrect_password_error() - Проверка ошибки некорректного пароля 

tests_authorization - Тесты на вход
    test_authorization_by_clicking_Log_in_to_account_home_page() - Позитивный тест на вход по кнопке «Войти в аккаунт» на главной
    test_authorization_through_Personal_Account_button() - Позитивный тест на вход через кнопку «Личный кабинет»
    test_authorization_button_in_registration_form() - Позитивный тест на вход через кнопку в форме регистрации
    test_authorization_button_in_password_recovery_form() - Позитивный тест на вход через кнопку в форме восстановления пароля

tests_transfer_to_personal_account - Тест для проверки перехода в личный кабинет
    test_transfer_to_personal_account_opens_personal_account_page - Позитивный тест на переход в личный кабинет

tests_transfer_from_personal_accaunt_to_constructor - Тест для проверки перехода с личного кабинета в конструктор
    test_transfer_from_personal_accaunt_to_constructor_by_clicking_constructor_header_transfer_constructor - Позитивный тест на переход из личного кабинета в конструктор по клику на "Конструктор"
    test_transfer_from_personal_accaunt_to_constructor_by_clicking_logo_transfer_constructor - Позитивный тест на переход из личного кабинета в конструктор по клику на логотип

tests_log_out_your_account - Тест для проверки входа из аккаунта
    test_log_out - Позитивный тест на выход из аккаунта

test_transitions_in_Constructor_section - Тесты переходов по разделам наполнения булок
    test_go_to_sauces_section_with_rolls_display_sauces - Позитивный тест перехода в раздел "Соусы" с раздела "Булки"
    test_go_to_sauces_section_with_fillings_display_sauces - Позитивный тест перехода в раздел "Соусы" с раздела "Начинки"
    test_go_to_fillings_section_with_rolls_display_fillings - Позитивный тест перехода в раздел "Начинки" с раздела "Булки"
    test_go_to_fillings_section_with_sauces_display_fillings - Позитивный тест перехода в раздел "Начинки" с раздела "Соусы"
    test_go_to_rolls_section_with_sauces_display_rolls - Позитивный тест перехода в раздел "Булки" с раздела "Соусы"
    test_go_to_rolls_section_with_fillings_display_rolls - Позитивный тест перехода в раздел "Булки" с раздела "Начинки"

helpers
    password_generation(linght) - Генерация пароля. Передается количество символов в пароле
    email_generation(cohort) - Генерация email. Передается номер когорты
    entering_data_for_registration(driver, email, password) - Заполнение полей для регистрации
    click_on_register_button(driver) - Клик по кнопке "Зарегестрироваться" в форме регистрации
    click_on_log_in_account_button(driver) - Клик по кнопке "Войти в аккаунт" на главной странице
    click_on_word_register(driver) - Клик по слову "Зарегестрироваться" для перехода в форму регистрации
    entering_data_log_in_to_account(driver, email, password) - заолнение полей для входа в аккаунт
    click_on_login_button(driver) - Клик по кнопке "Войти" на форме входа в аакаунт
    click_on_header_personal_account(driver) - Клик по хедеру "Личный переход" для перехода в личный кабинет
    click_on_word_log_in(driver) - Клик по кнопке "Войти" внизу страницы
    click_on_password_recovery_button(driver) - Клик по кнопке "Восстановление пароля" в форме входа в аккаунт
    click_on_header_сonstructor(driver) - Клик по хедеру "Конструктор"
    click_on_exit_button(driver) - Клик по кнопке "Выход" в личном кабинете
    click_sauce(driver) - Клик по вкладке соусы в конструкторе
    click_filling(driver) - Клик по вкладке начинки в конструкторе
    click_rolls(driver) - Клик по вкладке булки в конструкторе
    
    


