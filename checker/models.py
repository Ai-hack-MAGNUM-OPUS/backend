import uuid as uuid
from django.db import models

# Create your models here.


class Docx(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    file = models.FileField(upload_to="")

    def __str__(self):
        return self.uuid


class ParagraphType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Paragraph(models.Model):
    text = models.TextField()
    type = models.ForeignKey(
        ParagraphType, related_name="paragraphs", on_delete=models.CASCADE
    )
    docx = models.ForeignKey(Docx, related_name="paragraphs", on_delete=models.CASCADE)
