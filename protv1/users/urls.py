from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register('users-viewset', views.UsersViewSet, basename='users-viewset')
router.register('custom-users',views.CustomUserViewSet)
router.register('requests', views.ApplicationsViewSet)

urlpatterns = [
    path('login/', views.CustomUserLoginApiView.as_view()),
    path('', include(router.urls))
]