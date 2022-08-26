from rest_framework import serializers

from checker.models import Docx


class DocxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docx
        fields = ["uuid", "file"]
        extra_kwargs = {"uuid": {"read_only": True}}
