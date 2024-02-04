from django.urls import path

from .views import search_view, result_view, video_view

urlpatterns = [
    path("", search_view, name="search"),
    path("result", result_view, name="result"),
    path("video/<str:video_id>", video_view, name="video"),
]
