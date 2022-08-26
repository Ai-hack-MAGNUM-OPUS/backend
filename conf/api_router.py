from django.urls import path, include

from checker.api.views import ListCreateDocxApiView

urlpatterns = [
    path("health/", include("health_check.urls")),
    path("docx/", ListCreateDocxApiView.as_view(), name="list_create_docx")
]
