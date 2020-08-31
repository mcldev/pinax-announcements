from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from fontawesome.fields import IconField


class Announcement(models.Model):
    """
    A single announcement.
    """
    DISMISSAL_NO = 1
    DISMISSAL_SESSION = 2
    DISMISSAL_PERMANENT = 3

    DISMISSAL_CHOICES = [
        (DISMISSAL_NO, _("No Dismissals Allowed")),
        (DISMISSAL_SESSION, _("Session Only Dismissal")),
        (DISMISSAL_PERMANENT, _("Permanent Dismissal Allowed"))
    ]

    title = models.CharField(_("title"), max_length=100)
    content = models.TextField(_("content"))
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("creator"),
        on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField(_("creation_date"), default=timezone.now)
    enabled = models.BooleanField(_("enabled"), default=False)
    members_only = models.BooleanField(_("members only"), default=False)
    dismissal_type = models.IntegerField(choices=DISMISSAL_CHOICES, default=DISMISSAL_SESSION)
    publish_start = models.DateTimeField(_("publish_start"), default=timezone.now)
    publish_end = models.DateTimeField(_("publish_end"), blank=True, null=True)
    announcement_style = models.CharField(_("announcement style"), max_length=100, blank=True, null=True)
    icon = IconField(_("fontawesome icon"),)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def get_absolute_url(self):
        return reverse("pinax_announcements:announcement_detail", args=[self.pk])

    def dismiss_url(self):
        if self.dismissal_type != Announcement.DISMISSAL_NO:
            return reverse("pinax_announcements:announcement_dismiss", args=[self.pk])

    def is_enabled(self):
        if self.enabled and \
               self.publish_start <= timezone.now() and \
               (self.publish_end is None or self.publish_end >= timezone.now()):
            return True
        return False

    is_enabled.boolean = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("announcement")
        verbose_name_plural = _("announcements")
        ordering = ['order']


class Dismissal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="announcement_dismissals",
        on_delete=models.CASCADE
    )
    announcement = models.ForeignKey(
        Announcement,
        related_name="dismissals",
        on_delete=models.CASCADE
    )
    dismissed_at = models.DateTimeField(default=timezone.now)
