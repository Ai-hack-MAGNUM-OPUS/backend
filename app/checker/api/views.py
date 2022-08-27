from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

from checker.api.serializers import (
    DocxSerializer,
    DocxStateSerializer,
    WordDocxSerializer,
    WordDocxStateSerializer,
)
from checker.models import Docx, ParagraphType, WordDocx


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
        paragraphs = ParagraphType.objects.all()
        for p in paragraphs:
            res[p.name] = [(x.text, x.score) for x in p.paragraphs.filter(docx=doc)]
        return Response(res)


class ListCreateWordDocxApiView(generics.ListCreateAPIView):
    serializer_class = WordDocxSerializer
    queryset = WordDocx.objects.all()


class GetWordDocxState(generics.RetrieveAPIView):
    lookup_field = "uuid"
    queryset = WordDocx.objects.all()
    serializer_class = WordDocxStateSerializer


class RetireWordDocxSerializer(APIView):
    # TODO create base class
    def get(self, request, uuid):
        doc = get_object_or_404(WordDocx, uuid=uuid)
        res = {}
        paragraphs = ParagraphType.objects.all()
        for p in paragraphs:
            res[p.name] = [(x.text, x.score) for x in p.word_paragraphs.filter(docx=doc)]
        return Response(res)
