from django.urls import include, re_path
from django.http import HttpResponse


def dummy_view(request):
    return HttpResponse(content=b"", status=200)


urlpatterns = [
    re_path(r"^", include("pinax.announcements.urls")),
    re_path(r"^dummy_login/$", dummy_view, name="account_login"),
]
