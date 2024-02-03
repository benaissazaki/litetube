from django.urls import path

from .views import search_view, result_view

urlpatterns = [
    path("", search_view, name="search"),
    path("result", result_view, name="result"),
]
