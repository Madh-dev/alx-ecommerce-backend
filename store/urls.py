from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import( ProductViewSet, 
                   CategoryViewSet, 
                   UserRegisterView,
                   UserProfileView,
                   UserProfileUpdateView,
                   AdminUserViewSet
)
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r"users", AdminUserViewSet, basename="users") # admin-only

urlpatterns = [
    path('', include(router.urls)),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/update", UserProfileUpdateView.as_view(), name="profile-update"),
]
