from django.urls import path
from .views import all_list

urlpatterns = [
    path("", all_list, name="all_list"),
]
