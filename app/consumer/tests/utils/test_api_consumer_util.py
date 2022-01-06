import unittest
from consumer.utils import ApiConsumer


class ApiConsumerUtilTestCase(unittest.TestCase):

    def setUp(self):
        self.util = ApiConsumer()
        self.api_url = 'https://api.chucknorris.io/jokes/'

    def test_builds_url_with_no_arguments(self):
        url = self.util.build_url()
        self.assertEqual(url, self.api_url)

    def test_can_build_url_with_path_only(self):
        url = self.util.build_url('categories')
        self.assertEqual(url, f'{self.api_url}categories')

    def test_can_build_url_with_query(self):
        url = self.util.build_url(query='category', query_param='animal')
        self.assertEqual(url, f'{self.api_url}?category=animal')

    def test_can_get_categories(self):
        category = self.util.get_categories()
        self.assertTrue(len(category) > 1)

    def test_can_get_a_categories_content(self):
        content = self.util.search_content(query_param='animal')
        self.assertTrue(len(content) > 1)
