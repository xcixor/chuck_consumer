from django.urls import path
from consumer.presentation.views import HomeView

app_name = 'consumer'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
