from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),
    path('impressum/', views.impressum, name='impressum'),

    # Paraguay
    path('paraguay/strukturberatung/', views.py_strukturberatung, name='py_strukturberatung'),
    path('paraguay/investieren/', views.py_investieren, name='py_investieren'),
    path('paraguay/immobilien/', views.py_immobilien, name='py_immobilien'),
    path('paraguay/leben/', views.py_leben, name='py_leben'),
    path('paraguay/videos/', views.py_videos, name='py_videos'),

    # Paraguay Downloads
    path('paraguay/eas/', views.py_download_eas, name='py_download_eas'),
    path('paraguay/eas/danke/', views.py_download_eas_success, name='py_download_eas_success'),
    path('paraguay/steuern/', views.py_download_steuern, name='py_download_steuern'),
    path('paraguay/steuern/danke/', views.py_download_steuern_success, name='py_download_steuern_success'),
]
