import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cart_goods = "//button[@class='rb-btn cart-product__btn']"
    delete_btn = "//button[@class='rb-btn rb-btn_success float-right']"
    buket_in_cart = "//a[@class='cart-product__title']"
    order_button = "a[href='/ocheckout']"

    #Getters

    # Получаем список кнопок для удаления каждого товара в корзине
    def get_cart_goods(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_goods)))
        return self.driver.find_elements(By.XPATH, value= self.cart_goods)

    # Получаем кнопку
    def get_delete_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, self.delete_btn)))

    def get_buket_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, self.buket_in_cart))).text

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, self.order_button)))

    #Actions
    def click_order_button(self):
        self.get_order_button().click()


    def clear_cart(self):
        cart_goods_list = self.get_cart_goods()
        for cart_good in cart_goods_list:
            cart_good.click()
            self.get_delete_btn().click()
            time.sleep(1)
            # WebDriverWait(self.driver, 30).until(EC.invisibility_of_element((By.XPATH, "//*[@id='js_app-cart']/div/div[2]/div[4]/div[2]/div[2]/a")))
        self.driver.back()

