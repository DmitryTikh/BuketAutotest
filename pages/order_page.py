import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Order_page():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    #Locators
    sender_checkbox = ".order-form__group-title>.rb-form-check>span.rb-form-check__label"
    phone_number = "input[placeholder='Номер телефона *']"
    delivery_date = ".datepicker-input"
    delivery_time = '.noUi-base'
    dates = '.datepicker-cell'
    leftSlider = '.noUi-handle-lower>.noUi-touch-area'
    delivery_address = '.suggestions-input'

    #Variables
    our_address = 'ул Балтийская, д 11'
    our_phone_number = '79222321212'

    #Getters

    # Получаем чекбокс "Я сам получу заказ"
    def get_sender_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sender_checkbox)))

    # Получаем поле с номером клиента
    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.phone_number)))

    # Получаем поле с выбором дня доставки
    def get_delivery_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delivery_date)))

    # Получаем поле с выбором времени доставки
    def get_delivery_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delivery_time)))

    # Получаем левый ползунок
    def get_leftSlider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.leftSlider)))

    # Получаем адрес доставки
    def get_delivery_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delivery_address)))

    #Actions

    def click_sender_checkbox(self):
        self.get_sender_checkbox().click()

    def input_phone_number(self):
        self.get_phone_number().send_keys(self.our_phone_number)

    def input_delivery_address(self):
        delivery_address = self.get_delivery_address()
        delivery_address.click()
        delivery_address.send_keys(self.our_address)
        self.get_delivery_address()
        time.sleep(3)
        delivery_address.send_keys(Keys.ENTER)


    def input_delivery_date(self):
        self.get_delivery_date().click()
        days_in_month = self.driver.find_elements(By.CSS_SELECTOR, value = self.dates)
        for i in days_in_month:
            day = i.text
            if day == '25':
                i.click()
                break

    #Methods

    # Заполняем необходимые поля для оформления заказа
    def makeOrder(self):
        self.click_sender_checkbox()
        self.input_phone_number()
        self.input_delivery_date()
        startSlider = self.get_leftSlider()
        time.sleep(3)
        self.action.click_and_hold(startSlider).move_by_offset(170, 0).release().perform()
        time.sleep(3)
        self.input_delivery_address()
