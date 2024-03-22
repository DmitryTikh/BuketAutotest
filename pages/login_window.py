from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Login_window(Base):

    url = 'https://rus-buket.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    open_login_window = "//button[@id ='js_header-login']"
    login_field = "//input[@id ='js_login-email-or-phone']"
    password_field = "//input[@type ='password']"
    enter_button = "//button[@id ='js_btn-login']"
    received_user_name = "//div[@class='text-ellipsis js_header-user__user-name']"

    #Getters
    def get_open_login_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_login_window)))

    def get_login_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.received_user_name))).text

    #Actions

    # Открываем окно с авторизацией
    def click_open_login_window(self):
        self.get_open_login_window().click()
        print('Open login window')

    def input_user_login(self, user_login):
        self.get_login_field().send_keys(user_login)
        print('Input user login')

    def input_user_password(self, user_password):
        self.get_password_field().send_keys(user_password)
        print('Input user password')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Click enter_button')

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_open_login_window()
        self.input_user_login('retyantonsko@mail.ru')
        self.input_user_password('515761')
        self.click_enter_button()
        self.assert_user_name(self.get_user_name(), 'Алексей')