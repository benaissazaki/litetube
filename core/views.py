from django.shortcuts import render

from .forms import VideoSearchForm


def search_view(request):
    context = {"video_search_form": VideoSearchForm()}

    return render(request, "search.html", context)
