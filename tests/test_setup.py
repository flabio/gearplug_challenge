from faker import Faker
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        from apps.users.models import Account
       
        faker=Faker()
        self.logins_url='/login/'
     
       
        self.user=Account.objects.create_user(
            first_name=faker.name(),
            last_name=faker.last_name(),
            username=faker.user_name(),
            email=faker.email(),
            password="12345678",
        )
        url = reverse('login')
        data = {
               	"username":self.user.username,
	            "password":"12345678",
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.token=response.data['token']['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        return super().setUp()
    