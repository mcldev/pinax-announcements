from django.db.models.signals import pre_save
from .models import Announcement
from django.dispatch import receiver


@receiver(pre_save, sender=Announcement, dispatch_uid="update_announcement_ordering")
def update_ordering(sender, instance, **kwargs):
    if instance.id is None:
        announcements = Announcement.objects.all().exclude(id=instance.id)
        for annoucement in announcements:
            annoucement.order = annoucement.order + 1
        Announcement.objects.bulk_update(announcements, ['order'])


