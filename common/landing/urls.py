from django.urls import path
from common.landing import views

urlpatterns = [
    path('settings/',views.SettingsAPIVew.as_view()),
    
]
