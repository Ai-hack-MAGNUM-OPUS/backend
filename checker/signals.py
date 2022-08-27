from django.db.models.signals import post_save
from django.dispatch import receiver

from checker.models import Docx, WordDocx
from checker.tasks import process_file, process_word


@receiver(post_save, sender=Docx)
def create_docs(sender, instance, created, **kwargs):
    if created:
        process_file.apply_async(kwargs={"pk": instance.pk})
        return


@receiver(post_save, sender=WordDocx)
def create_docs(sender, instance, created, **kwargs):
    if created:
        process_word.apply_async(kwargs={"pk": instance.pk})
        return

