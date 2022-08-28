import magic

from django.db.models.signals import post_save
from django.core.files import File
from django.dispatch import receiver
from celery import chain

from checker.models import Docx, WordDocx
from checker.services.file import doc_to_docx, doc_to_odt
from checker.tasks import process_file, process_word, highlight_file


@receiver(post_save, sender=Docx)
def create_docs(sender, instance, created, **kwargs):
    if created:
        type = magic.from_file(instance.file.path, mime=True)
        if type == "application/msword":
            pth = doc_to_docx(instance.file.path)
            with open(pth, 'rb') as f:
                instance.file = File(f, name=pth.split("/")[-1])
                instance.save(update_fields=["file"])
        elif type == "application/vnd.oasis.opendocument.text":
            pth = doc_to_odt(instance.file.path)
            with open(pth, 'rb') as f:
                instance.file = File(f, name=pth.split("/")[-1])
                instance.save(update_fields=["file"])

        chain(process_file.s(instance.pk), highlight_file.s()).apply_async()
        return


@receiver(post_save, sender=WordDocx)
def create_docs(sender, instance, created, **kwargs):
    if created:
        process_word.apply_async(kwargs={"pk": instance.pk})
        return

