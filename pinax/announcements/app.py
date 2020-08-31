from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AnnouncementsConfig(AppConfig):
    name = 'pinax.announcements'
    verbose_name = _('Announcements')

    def ready(self):
        import pinax.announcements.receivers
