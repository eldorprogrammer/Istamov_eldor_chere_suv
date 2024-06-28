from django.urls import path,include
from product.landing import views
urlpatterns = [
    path('products/',views.ProductGetAPIView.as_view()),
]

