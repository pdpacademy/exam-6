from django.urls import path

from apps import views
from apps.views import RegisterTemplateView

urlpatterns = [
    path('', views.index, name='index_page'),
    path('register/', RegisterTemplateView.as_view(), name='register_page'),
]