from rest_framework import serializers

from checker.models import Docx, WordDocx


class DocxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docx
        fields = ["uuid", "file"]
        extra_kwargs = {"uuid": {"read_only": True}}


class DocxStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docx
        fields = ["paragraphs_loaded", "paragraphs_processed"]


class WordDocxSerializer(serializers.ModelSerializer):
    text = serializers.CharField()

    class Meta:
        model = WordDocx
        fields = ["text", "uuid"]
        extra_kwargs = {"uuid": {"read_only": True}, "text": {"write_only": True}}
        write_only = ["text"]

    def validate_text(self, val):
        return str(val).encode()


class WordDocxStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordDocx
        fields = ["paragraphs_loaded", "paragraphs_processed"]
