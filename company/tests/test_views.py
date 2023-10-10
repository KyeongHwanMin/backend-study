from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from company.models import Company


class CompanyTest(APITestCase):
    def test_create_company(self):
        url = '/api/v1/company'
        data = {
            'company_name': '원티드',
            'nation': '한국',
            'area': '서울'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()

        company = Company.objects.get()
        self.assertEqual(response_json['id'], company.id)
        self.assertEqual(response_json['company_name'], company.company_name)
        self.assertEqual(response_json['nation'], company.nation)
        self.assertEqual(response_json['area'], company.area)
