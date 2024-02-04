from django.shortcuts import render
import pytube
from .forms import VideoSearchForm


def search_view(request):
    context = {"video_search_form": VideoSearchForm()}

    return render(request, "search.html", context)


def result_view(request):
    search_query = request.GET.get("query")
    search = pytube.Search(search_query)

    context = {"search_results": search.results}
    return render(request, "result.html", context)


def video_view(request, video_id):
    context = {"video_id": video_id}

    return render(request, "video.html", context)
