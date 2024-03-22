import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    def get_screenshot(self):
        now_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_data + '.png'
        self.driver.save_screenshot('C:\\Users\\Дмитрий\\PycharmProjects\\rusBuketProject\\screen\\' + name_screenshot)

    def assert_user_name(self, received_user_name, result_user_name):
        assert received_user_name == result_user_name
        print('Good User name')

    def assert_cart_product(self, buket_in_cart, chosen_buket_name):
        if buket_in_cart in chosen_buket_name:
            print('Букет в корзине верный')
        else:
            raise IOError("Букет, который мы выбрали не соотвествует букету в корзине")