from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver, cart_page):
        super().__init__(driver)
        self.driver = driver
        self.cart_page = cart_page

    #Locators
    cookies_close_button = "//div[@id='js_gdpr__btn-close']"
    birth_day = "div#js_catalog-tags>a[href='/catalog/birthday']"
    priceEnd = "//input[@id='js_rb-filter__price-to']"
    kind_of_flowers = "div[data-code='flowers']>div.rb-filter__group-header"
    tulips_checkbox = "input[value='58']+span.rb-form-check__label"
    lilies_checkbox = "input[value='60']+span.rb-form-check__label"
    recipient = "div[data-code='whom']>div.rb-filter__group-header"
    mother_checkbox = "input[value='95']+a[href='/catalog/mom/birthday']"
    buket_style = "div[data-code='color']>div.rb-filter__group-header"
    style_gentle_checkbox = "input[value='81']+span.rb-form-check__label"
    style_author_checkbox = "input[value='168']+span.rb-form-check__label"
    buket_type = "div[data-code='buket_type']>div.rb-filter__group-header"
    composition_checkbox = "input[value='23']+a[href='/catalog/birthday']"
    button_buy = "//button[@data-id='5316']"
    chosen_buket_name = "div[data-id='5316']>a.rb-product-card__name"
    button_cart = "//a[@class='header__btn header-middle__btn header-cart d-none d-lg-flex']"
    cart_number_of_products = "//span[@class='header-cart__qty js_cart-qty ']"

    #Getters

    def get_cookies_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookies_close_button)))

    def get_birth_day(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.birth_day)))

    def get_priceEnd(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.priceEnd)))

    def get_kind_of_flowers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.kind_of_flowers)))

    def get_tulips_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.tulips_checkbox)))

    def get_lilies_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.lilies_checkbox)))

    def get_recipient(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.recipient)))

    def get_mother_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.mother_checkbox)))

    def get_buket_style(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.buket_style)))

    def get_style_gentle_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.style_gentle_checkbox)))

    def get_style_author_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.style_author_checkbox)))

    def get_buket_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.buket_type)))

    def get_composition_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.composition_checkbox)))

    def get_button_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_chosen_buket_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.chosen_buket_name))).text

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))


    def get_cart_number_of_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_number_of_products)))

    #Actions

    def close_cookies_window(self):
        self.get_cookies_close_button().click()

    # Выбираем фильтр - День рождения
    def click_birth_day(self):
        self.get_birth_day().click()

    # Заполняем цену - стоимость не более 15000
    def input_priceEnd(self):
        priceEnd_field = self.get_priceEnd()
        priceEnd_field.click()
        priceEnd_field.send_keys(Keys.CONTROL + "a")
        priceEnd_field.send_keys(Keys.BACKSPACE)
        priceEnd_field.send_keys('15000')
        priceEnd_field.send_keys(Keys.ENTER)

    # Открываем фильтр "Цветы"
    def click_kind_of_flowers(self):
        self.get_kind_of_flowers().click()

    # Выбираем содержание тюльпанов в фильтре "Цветы"
    def click_tulips_checkbox(self):
        self.get_tulips_checkbox().click()

    # Выбираем содержание лилий в фильтре "Цветы"
    def click_lilies_checkbox(self):
        self.get_lilies_checkbox().click()

    # Открываем фильтр "Кому"
    def click_recipient(self):
        self.get_recipient().click()

    # Выбираем "Маме" в фильтре "Кому"
    def click_mother_checkbox(self):
        self.get_mother_checkbox().click()

    # Открываем фильтр "Стиль"
    def click_buket_style(self):
        self.get_buket_style().click()

    # Выбираем "Нежный" в фильтре "Стиль"
    def click_style_gentle_checkbox(self):
        self.get_style_gentle_checkbox().click()

    # Выбираем "Авторский" в фильтре "Стиль"
    def click_style_author_checkbox(self):
        self.get_style_author_checkbox().click()

    # Открываем фильтр "Тип букета"
    def click_buket_type(self):
        self.get_buket_type().click()

    # Выбираем "Композиции" в фильтре "Тип букета"
    def click_bucket_type_checkbox(self):
        self.get_composition_checkbox().click()

    # Кликаем "Заказать" напротив букета "Сиреневые тюльпаны"
    def click_button_buy(self):
        self.get_button_buy().click()

    # Переходим в корзину
    def click_button_cart(self):
        self.get_button_cart().click()

    # Кликаем на число заказанных товаров, отображающих напротив корзины, когда она не пуста
    def click_cart_number_of_products(self):
        self.get_cart_number_of_products().click()

    #Methods

    # Выбираем букет для Мамы на День рождения, переходим в корзину
    # и проверяем соответствует ли букет в корзине, выбранному нами в каталоге
    def chose_product(self):
        self.click_birth_day()
        self.input_priceEnd()
        self.click_kind_of_flowers()
        self.click_tulips_checkbox()
        self.click_lilies_checkbox()
        self.click_recipient()
        self.click_mother_checkbox()
        self.click_buket_style()
        self.click_style_gentle_checkbox()
        self.click_style_author_checkbox()
        self.click_buket_type()
        self.click_bucket_type_checkbox()
        self.driver.refresh()
        chosen_buket = self.get_chosen_buket_name()
        self.click_button_buy()
        self.click_button_cart()
        product_in_cart = self.cart_page(self.driver).get_buket_in_cart()
        self.assert_cart_product(product_in_cart, chosen_buket )
        self.get_screenshot()
        self.cart_page(self.driver).click_order_button()
    # Итоговая функция по выбору букета согласно фильтрам и отправка букета в корзину
    def select_product(self):
        # закрываем окно с предупреждением о сохранении Cookies
        self.close_cookies_window()
        # Обновляем страницу т.к. после авторизации напротив корзины не отображается информация о том,
        # что в ней что то есть, после обновления все ОК
        self.driver.refresh()
        # Если напротив корзины есть поле с числом товаров в ней, то переходим в корзину, очищаем ее
        # далее возвращаемся в каталог и выбираем нужный нам букет
        try:
            self.click_cart_number_of_products()
            self.cart_page(self.driver).clear_cart()
            self.driver.refresh()
            self.chose_product()
        except TimeoutException:
            self.chose_product()




