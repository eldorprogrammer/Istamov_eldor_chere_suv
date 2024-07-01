from django.urls import path
from common.landing import views

urlpatterns = [
    path('settings/',views.SettingsAPIVew.as_view()),
    path('photos/', views.GaleryPhotoRandomAPIView.as_view()),
    path('page/retrieve/<slug:slug>/', views.PageAPIView.as_view()),

]
