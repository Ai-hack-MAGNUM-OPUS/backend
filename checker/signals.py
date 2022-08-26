from pprint import pprint
import requests

import docx2txt
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from checker.models import Docx
from checker.services.file import process_paragraphs


@receiver(post_save, sender=Docx)
def create_docs(sender, instance, created, **kwargs):
    if created:
        document = docx2txt.process(instance.file.path)
        paragraphs = process_paragraphs(document.split("\n"))
        x = requests.post(settings.AI_URL, json=paragraphs)
        return
