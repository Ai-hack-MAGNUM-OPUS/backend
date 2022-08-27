from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

from checker.api.serializers import DocxSerializer, DocxStateSerializer
from checker.models import Docx, ParagraphType


class ListCreateDocxApiView(generics.ListCreateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = DocxSerializer
    queryset = Docx.objects.all()


class GetDocxState(generics.RetrieveAPIView):
    lookup_field = "uuid"
    queryset = Docx.objects.all()
    serializer_class = DocxStateSerializer


class RetireDocxSerializer(APIView):
    def get(self, request, uuid):
        doc = get_object_or_404(Docx, uuid=uuid)
        res = {}
        paragraphs = ParagraphType.objects.filter(paragraphs__docx=doc)
        for p in paragraphs:
            res[p.name] = [x.text for x in p.paragraphs.filter(docx=doc)]
        return Response(res)

