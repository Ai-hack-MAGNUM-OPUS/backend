from time import sleep

import docx2txt
import requests
from celery import shared_task

from django.conf import settings

from checker.models import Paragraph, Docx
from checker.services.file import process_paragraphs


@shared_task()
def process_file(pk: int):
    file = Docx.objects.get(pk=pk)
    document = docx2txt.process(file.file.path)
    paragraphs = process_paragraphs(document.split("\n"))

    file.paragraphs_loaded = len(paragraphs)
    file.save(update_fields=["paragraphs_loaded"])

    x = requests.post("http://185.244.175.164:5000/api", json=paragraphs)
    for el_id, type_id in x.json().items():
        Paragraph.objects.create(
            type_id=type_id, docx=file, text=paragraphs[el_id]
        )

    file.paragraphs_processed = len(paragraphs)
    file.save(update_fields=["paragraphs_processed"])

    return file

