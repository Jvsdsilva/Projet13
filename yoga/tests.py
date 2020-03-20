from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from yoga.forms import RegistrationForm
from django.views.generic import TemplateView
from yoga.models import UploadImage, Events
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Models test
class EntryModelTest(TestCase):

    def test_UploadImage(self):
        entry = UploadImage(title="Default")
        self.assertEqual(str(entry), entry.title)

    def test_Events(self):
        entry = Events(title="Default")
        self.assertEqual(str(entry), entry.title)


# form test
class CommentFormTest(TestCase):

    def test_valid_data(self):
        form = RegistrationForm(data={"username": "jspurbeurre",
                                      "email": "purbeurre@example.com",
                                      "password1": "pass1234.",
                                      "password2": "pass1234."
                                      })

        self.assertTrue(form.is_valid())

    def test_non_valid_data(self):
        form = RegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)


class HomeView(TemplateView):
    template_name = 'yoga/index.html'

    def get_context_data(self, **kwargs):
        kwargs['environment'] = 'Production'
        return super().get_context_data(**kwargs)


# views test
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.login = reverse('login')
        self.logout = reverse('logout')
        self.signup = reverse('signup')
        self.gimyoga = reverse('gimyoga')
        self.gigong = reverse('gigong')
        self.professeur = reverse('professeur')
        self.cours = reverse('cours')
        self.contact = reverse('contact')
        self.blog = reverse('blog')
        self.upload = reverse('upload')
        self.addEvent = reverse('addEvent')

    def test_index_GET(self):
        response = self.client.post(self.index)

        def setUp(self):
            # Every test needs access to the request factory.
            self.user = User.objects.create_user(
                username='joana', email='joana@gmail.com',
                password='top_secret')

        def test_user(self):

            request.user = self.user

            if self.user == 'admin':
                self.assertTemplateUsed(response, 'yoga/index_admin.html')
            else:
                self.assertTemplateUsed(response, 'yoga/index.html')

    def test_login_GET(self):
        response = self.client.get(self.login)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/login.html')

    def test_logout_POST(self):
        response = self.client.post(self.logout)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/index.html')

    def test_signup_POST(self):
        response = self.client.post(self.signup)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/signup.html')

    def test_gimyoga_GET(self):
        response = self.client.get(self.gimyoga)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/gim_yoga.html')

    def test_gigong_GET(self):
        response = self.client.get(self.gigong)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/gi_gong.html')

    def test_professeur_GET(self):
        response = self.client.get(self.professeur)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/professeur.html')

    def test_cours_GET(self):
        response = self.client.get(self.cours)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/cours.html')

    def test_contact_GET(self):
        response = self.client.get(self.contact)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/contact.html')

    def test_blog_GET(self):
        response = self.client.get(self.blog)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/blog.html')

    def test_upload_GET(self):
        response = self.client.get(self.upload)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/simple_upload.html')

    def test_addEvent_GET(self):
        response = self.client.get(self.addEvent)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'yoga/add_event.html')


# selenium test uploads
@pytest.mark.usefixtures('driver')
class TestTestimage():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testimage(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1920, 1040)
        self.driver.find_element(By.CSS_SELECTOR, ".fas").click()
        self.driver.find_element(By.ID, "id_username").send_keys("admin")
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("admin1234")
        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "upload").click()
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys("image3")
        self.driver.find_element(By.NAME, "myfile").click()
        self.driver.find_element(By.NAME, "myfile").send_keys(
                                 "C:\\fakepath\\taichi-park.jpg")
        self.driver.find_element(By.ID, "upload").click()
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()


@pytest.mark.usefixtures('driver')
class TestTestevenements():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testevenements(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".nav-item:nth-child(6) > .nav-link").click()
        self.driver.find_element(By.ID, "blog").click()
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys(
                                "Sortie Plantes Médicinales")
        self.driver.find_element(By.NAME, "text").click()
        self.driver.find_element(By.NAME, "text").send_keys(
                                "Venez nombreux pour cette sortie en plein " +
                                "nature. Venez connaitre le meilleur de " +
                                "nos plantes. Cette sortie ce déroulera " +
                                "le 27 mars. Plus d’informations veuillez " +
                                "contacter Joana au contact@yoga.fr")
        self.driver.find_element(By.NAME, "myfile").click()
        self.driver.find_element(By.NAME, "myfile").send_keys(
                                "C:\\fakepath\\images.jpg")
        self.driver.find_element(By.ID, "ajouter").click()
