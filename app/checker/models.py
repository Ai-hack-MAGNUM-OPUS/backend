import uuid as uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from checker.services.file import media_upload_path


class Docx(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    file = models.FileField(upload_to=media_upload_path)
    created = models.DateTimeField(auto_now_add=True)

    paragraphs_processed = models.IntegerField(default=0)
    paragraphs_loaded = models.IntegerField(default=0)

    def __str__(self):
        return str(self.uuid)

    class Meta:
        ordering = ["-created"]


class WordDocx(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    text = models.BinaryField()
    created = models.DateTimeField(auto_now_add=True)

    paragraphs_processed = models.IntegerField(default=0)
    paragraphs_loaded = models.IntegerField(default=0)

    def __str__(self):
        return str(self.uuid)

    class Meta:
        ordering = ["-created"]


class ParagraphType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Paragraph(models.Model):
    score = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    text = models.TextField()
    type = models.ForeignKey(
        ParagraphType, related_name="paragraphs", on_delete=models.CASCADE
    )
    docx = models.ForeignKey(Docx, related_name="paragraphs", on_delete=models.CASCADE)


class WordParagraph(models.Model):
    text = models.TextField()
    type = models.ForeignKey(
        ParagraphType, related_name="word_paragraphs", on_delete=models.CASCADE
    )
    score = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    docx = models.ForeignKey(
        WordDocx, related_name="paragraphs", on_delete=models.CASCADE
    )
