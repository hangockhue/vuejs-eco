from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .user_api import MyTokenObtainPairView
from .ecommerce_api import CategoryViewSet, ProductViewSet

urlpatterns = [
    # Your URLs...
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', MyTokenObtainPairView.as_view()),
    path('api/categorys/', CategoryViewSet.as_view(), name='categorys'),
    path('api/products/', ProductViewSet.as_view(), name='products')
]