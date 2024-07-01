from django.urls import path
from product import views




urlpatterns = [
    path('listAPIView/',views.ProductListAPIView.as_view()),
    path('retrieveUpdateAPIView/<int:pk>/', views.ProductUpdateAPIView.as_view()),
    path('createAPIView/', views.ProductCreateAPIView.as_view()),
    path('retrieveAPIView/<int:pk>/', views.ProductRetrieveAPIView.as_view()),
    path('retrieveDestroyAPIView/<int:pk>/', views.ProductDestroyAPIView.as_view()),
    
]


