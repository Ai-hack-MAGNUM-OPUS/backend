from django.urls import path, include

from checker.api.views import ListCreateDocxApiView, RetireDocxSerializer, GetDocxState

urlpatterns = [
    path("health/", include("health_check.urls")),
    path(
        "site/",
        include(
            [
                path("docx/", ListCreateDocxApiView.as_view(), name="list_create_docx"),
                path(
                    "docx/<uuid:uuid>", RetireDocxSerializer.as_view(), name="get_docx"
                ),
                path(
                    "state/<uuid:uuid>", GetDocxState.as_view(), name="get_state_docx"
                ),
            ]
        ),
    ),
    path(
        "word/",
        include(
            [
                path("docx/", ListCreateDocxApiView.as_view(), name="list_create_word"),
                path(
                    "docx/<uuid:uuid>", RetireDocxSerializer.as_view(), name="get_word"
                ),
                path(
                    "state/<uuid:uuid>", GetDocxState.as_view(), name="get_state_word"
                ),
            ]
        ),
    ),
]
