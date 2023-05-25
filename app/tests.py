# from django.test import TestCase

# # Create your tests here.


import pytest
from  rest_framework.test import APIClient, APITestCase
from .models import Student
from django.urls import reverse


client = APIClient()

class MyViewTests(APITestCase):
    def test_get_all_student(self):
        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_create_student(self):
        url = ""
        payload = {
            "name": "paras",
            "email": "paras@gmail.com",
            "phn_no": 121212
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, payload)
