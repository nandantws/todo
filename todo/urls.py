from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, TodoCollectionViewSet

router = DefaultRouter()
router.register('todos', TodoCollectionViewSet,basename='todos')

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login')
]

urlpatterns += router.urls
