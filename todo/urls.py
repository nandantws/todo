from django.urls import path
from .views import RegisterView, LoginView, TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task', TodoViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]

urlpatterns += router.urls
