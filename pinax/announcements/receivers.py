from django.db.models.signals import post_save
from .models import Announcement
from django.dispatch import receiver

@receiver(post_save, sender=Announcement, dispatch_uid="update_announcement_ordering")
def update_ordering(sender, instance, **kwargs):
    announcements = Announcement.objects.all().exclude(id=instance.id)
    for annoucement in announcements:
        annoucement.order = annoucement.order + 1
    Announcement.objects.bulk_update(announcements, ['order'])


