from celery import shared_task

from checker.models import Docx


@shared_task
def process_file(file: Docx):
    return
