from django.urls import path
from consumer.presentation.views import (
    HomeView, GetCategoryContentView)

app_name = 'consumer'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:query_param>/', GetCategoryContentView.as_view(), name='home'),
]
