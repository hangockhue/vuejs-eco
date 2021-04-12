from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .user_api              import MyTokenObtainPairView
from .ecommerce_api         import CategoryViewSet, ProductViewSet, OrderViewSet, ProductDetailViewSet
from .views                 import UserAPI
urlpatterns = [
    # Your URLs...
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', MyTokenObtainPairView.as_view()),
    path('user/<int:pk>', UserAPI.as_view(), name='user_information'),
    path('api/categorys/', CategoryViewSet.as_view(), name='categorys'),
    path('api/products/', ProductViewSet.as_view(), name='products'),
    path('api/products/<int:pk>', ProductDetailViewSet.as_view(), name='productdetail'),
    path('api/order/', OrderViewSet.as_view(), name="order"),
]