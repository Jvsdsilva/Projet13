
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('admin1234')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

    def test_testimage(self):
        self.selenium.get("http://127.0.0.1:8000/")
        self.selenium.set_window_size(1920, 1040)
        self.selenium.find_element(By.CSS_SELECTOR, ".fas").click()
        self.selenium.find_element(By.ID, "id_username").send_keys("admin")
        self.selenium.find_element(By.ID, "id_password").click()
        self.selenium.find_element(By.ID, "id_password").send_keys("admin1234")
        self.selenium.find_element(By.ID, "login").click()
        self.selenium.find_element(By.ID, "upload").click()
        self.selenium.find_element(By.NAME, "title").click()
        self.selenium.find_element(By.NAME, "title").send_keys("image3")
        self.selenium.find_element(By.NAME, "myfile").click()
        self.selenium.find_element(By.NAME, "myfile").send_keys(
                                   "C:\\fakepath\\taichi-park.jpg")
        self.selenium.find_element(By.ID, "upload").click()
        self.selenium.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()

    def test_testevenements(self):
        self.selenium.get("http://127.0.0.1:8000/")
        self.selenium.set_window_size(1936, 1056)
        self.selenium.find_element(By.CSS_SELECTOR,
                                   ".nav-item:nth-child(6) >" +
                                   " .nav-link").click()
        self.selenium.find_element(By.ID, "blog").click()
        self.selenium.find_element(By.NAME, "title").click()
        self.selenium.find_element(By.NAME, "title").send_keys(
                                   "Sortie Plantes Médicinales")
        self.selenium.find_element(By.NAME, "text").click()
        self.selenium.find_element(By.NAME, "text").send_keys(
                                "Venez nombreux pour cette sortie en plein " +
                                "nature. Venez connaitre le meilleur de " +
                                "nos plantes. Cette sortie ce déroulera " +
                                "le 27 mars. Plus d’informations veuillez " +
                                "contacter Joana au contact@yoga.fr")
        self.selenium.find_element(By.NAME, "myfile").click()
        self.selenium.find_element(By.NAME, "myfile").send_keys(
                                   "C:\\fakepath\\images.jpg")
        self.selenium.find_element(By.ID, "ajouter").click()
