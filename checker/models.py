import uuid as uuid
from django.db import models

# Create your models here.


class Docx(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    file = models.FileField(upload_to="")
