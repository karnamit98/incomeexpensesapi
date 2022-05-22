from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()
        
        email = self.fake.email(),
        self.user_data = {
            'email':email,
            'username':email.split('@')[0],
            'password':email,
        }
        
        return super().setUp()
        
    def tearDown(self) -> None:
        return super().tearDown()