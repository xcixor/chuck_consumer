import json
from django.test import TestCase


class GetCategoryContentTestCase(TestCase):

    def test_successful_ajax_request_returns_expected_data(self):
        response = self.client.get(
            '/animal/',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(response.status_code, 200)
        response = json.loads(response.content)

    def test_http_request_returns_successfully(self):
        response = self.client.get(
            '/animal/',
        )
        self.assertEqual(response.status_code, 200)
