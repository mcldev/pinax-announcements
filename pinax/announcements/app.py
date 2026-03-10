from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AnnouncementsConfig(AppConfig):
    name = 'pinax.announcements'
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = _('Announcements')

    def ready(self):
        import pinax.announcements.receivers
