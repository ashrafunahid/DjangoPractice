from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month_name>", views.month_number_view),
    path("<str:month_name>", views.month_name_view, name="month-path"),
]