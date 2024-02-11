import json
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
    video = pytube.YouTube(f"http://youtube.com/watch?v={video_id}")
    streams = (
        video.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
    )
    streams_dict = {}
    for stream in streams:
        streams_dict[stream.resolution] = stream.url

    audio_stream = video.streams.filter(only_audio=True).first().url
    context = {"video": video, "streams": streams, "streams_json": json.dumps(
        streams_dict), "audio_stream_url": audio_stream}

    return render(request, "video.html", context)
