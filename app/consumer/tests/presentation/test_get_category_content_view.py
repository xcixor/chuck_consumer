from django.test import TestCase
from django.views import View
from consumer.presentation.views import GetCategoryContentView


class GetCategoryContentViewTestCase(TestCase):

    def test_view_properties(self):
        self.assertTrue(issubclass(GetCategoryContentView, View))
