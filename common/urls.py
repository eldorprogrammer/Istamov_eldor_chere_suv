from django.urls import path,include
from common import views

urlpatterns = [

  
    path('settings/',views.SettingsGetEditAPIView.as_view()),
    path('galeryphoto/list/', views.GaleryPhotoListAPIView.as_view()),
    path('galeryphoto/create/', views.GaleryPhotoCreateAPIView.as_view()),
    path('galeryphoto/retrievedestroy/', views.GaleryPhotoRetrieveDestroyAPIView.as_view()),

]
