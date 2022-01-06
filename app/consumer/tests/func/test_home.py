from django.test import TestCase


class HomeTestCase(TestCase):

    def test_successfully_gets_home_url(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, 'home/home.html')

    def test_adds_categories_to_context(self):
        result = self.client.get('/')
        self.assertTrue(result.context.get('categories'))
