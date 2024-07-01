from django.urls import path
from order.landing import views



urlpatterns = [
    path('orderlist/', views.OrderListApiView.as_view()),
]
