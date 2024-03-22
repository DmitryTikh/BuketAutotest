from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_page
from pages.login_window import Login_window
from pages.main_page import Main_page
from pages.order_page import Order_page


def test_order_buket(set_up, set_group):

    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    # Убираем предупреждения об ошибках с SSL
    options.add_argument('log-level=3')
    g = Service('C:\\Users\\Дмитрий\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_window(driver)
    login.authorization()

    mp = Main_page(driver, Cart_page)
    mp.select_product()

    our_order = Order_page(driver)
    our_order.makeOrder()