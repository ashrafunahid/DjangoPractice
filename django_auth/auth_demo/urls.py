from django.urls import path
from .views import index, register, login, logout, delete_account, change_password

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('delete-account/', delete_account, name="delete-account"),
    path('change-password/', change_password, name="change-password"),
]
