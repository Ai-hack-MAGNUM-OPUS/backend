from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from checker.api.serializers import DocxSerializer
from checker.models import Docx


class ListCreateDocxApiView(generics.ListCreateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = DocxSerializer
    queryset = Docx.objects.all()
