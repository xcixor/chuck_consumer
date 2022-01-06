from django.test import TestCase
from django.views.generic import TemplateView
from consumer.presentation.views import HomeView


class HomeViewTestCase(TestCase):

    def test_view_properties(self):
        self.assertEqual(HomeView.template_name, 'home/home.html')
        self.assertTrue(issubclass(HomeView, TemplateView))
