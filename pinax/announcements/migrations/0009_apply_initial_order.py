# Generated by Django 2.2.15 on 2020-08-27 09:29

from django.db import migrations, models


def reorder(apps, schema_editor):
    AnnouncementModel = apps.get_model("announcements", "Announcement")
    announcements = AnnouncementModel.objects.all().order_by('-creation_date')
    order = 0
    for item in announcements:
        item.order = order
        order += 1
    AnnouncementModel.objects.bulk_update(announcements, ['order'])

class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0008_auto_20200902_1024'),
    ]

    operations = [
        migrations.RunPython(reorder, reverse_code=migrations.RunPython.noop),
    ]