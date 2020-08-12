from django.test import TestCase, Client
from http import HTTPStatus


class ForecastTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_location_not_found(self):
        args = {'country': 'not-exist', 'city': 'not-exist'}
        r = self.client.get('/forecast/', args)
        self.assertEqual(r.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def test_ok(self):
        args = {'country': 'Russia', 'city': 'Moscow'}
        r = self.client.get('/forecast/', args)
        self.assertEqual(r.status_code, HTTPStatus.OK)

    def test_russian_language(self):
        args = {'country': 'Россия', 'city': 'Москва'}
        r = self.client.get('/forecast/', args)
        self.assertEqual(r.status_code, HTTPStatus.OK)

    def test_no_city(self):
        args = {'country': 'Russia'}
        r = self.client.get('/forecast/', args)
        self.assertEqual(r.status_code, HTTPStatus.OK)