from django.db.models.signals import post_save
from django.dispatch import receiver

from checker.models import Docx
from checker.tasks import process_file


@receiver(post_save, sender=Docx)
def create_player(sender, instance, created, **kwargs):
    if created:
        process_file.delay(file=instance)
        return
