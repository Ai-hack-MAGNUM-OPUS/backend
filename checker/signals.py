import asyncio

import docx2txt
from django.db.models.signals import post_save
from django.dispatch import receiver

from checker.models import Docx, Paragraph
from checker.services.file import process_paragraphs
from checker.tasks import process_file
import threading
import asyncio


@receiver(post_save, sender=Docx)
def create_docs(sender, instance, created, **kwargs):
    if created:
        process_file.apply_async((instance.pk))
        return
