from typing import Type

from django.dispatch import receiver
from video_encoding import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rq import enqueue

from video_encoding import tasks

from .models import MontageVideoGallery


@receiver(post_save, sender=MontageVideoGallery)
def convert_video(sender, instance, **kwargs):
    enqueue(tasks.convert_all_videos,
            instance._meta.app_label,
            instance._meta.model_name,
            instance.pk)


@receiver(signals.encoding_finished, sender=MontageVideoGallery)
def mark_as_finished(sender: Type[MontageVideoGallery], instance: MontageVideoGallery) -> None:
    """
    Mark video as "convertion has been finished".
    """
    MontageVideoGallery.processed = True
    MontageVideoGallery.save(update_fields=['processed'])
