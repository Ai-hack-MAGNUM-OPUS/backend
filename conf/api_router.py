from django.urls import path, include

from checker.api.views import ListCreateDocxApiView, RetireDocxSerializer, GetDocxState

urlpatterns = [
    path("health/", include("health_check.urls")),
    path("docx/", ListCreateDocxApiView.as_view(), name="list_create_docx"),
    path("docx/<uuid:uuid>", RetireDocxSerializer.as_view(), name="get_docx"),
    path("state/<uuid:uuid>", GetDocxState.as_view(), name="get_state_docx"),
]
