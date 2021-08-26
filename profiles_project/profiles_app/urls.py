from django.urls import path, include
from profiles_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Hello-viewset', views.HelloViewSet, basename='hello_viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view()),
    path('',include(router.urls)),
]