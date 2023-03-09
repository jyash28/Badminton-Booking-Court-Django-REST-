from django.urls import path
from rest_framework.routers import DefaultRouter

from user import views

app_name = 'user'

router = DefaultRouter()
router.register('register', views.SignUpView, basename='signup')
router.register('user-list', views.UserListView, basename='user_list')
urlpatterns = [
    # path("register/", SignpView.as_view(), name='signup'),
    path("login/", views.LoginView.as_view(), name='login')
]

urlpatterns += router.urls
