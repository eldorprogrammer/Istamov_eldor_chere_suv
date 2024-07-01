from django.urls import path
from order import views


urlpatterns = [
    path('list/', views.OrderListAPIView.as_view()),
    path('retrieve/', views.OrderRetrieveAPIView.as_view()),
    path('edit/', views.OrderEditAPIView.as_view()),
]
