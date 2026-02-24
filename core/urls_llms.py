from django.urls import path
from . import views

urlpatterns = [
    path('', views.llms_txt, name='llms_txt'),
]
