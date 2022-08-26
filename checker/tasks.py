from celery import shared_task
from uuid import uuid4

from checker.models import Docx


@shared_task(name="process_file")
def process_file(file: uuid4):
    print(file)
    return file
