from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.contrib.auth import get_user_model
from pinax.announcements.forms import AnnouncementForm

from .filters import IsEnabledFilter
from .models import Announcement, Dismissal


class AnnouncementAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "creator", "creation_date", "is_enabled", "members_only")
    list_filter = (IsEnabledFilter, "members_only", )
    form = AnnouncementForm
    fieldsets = [
        (None, {
            "fields": [
                "title",
                ("icon", "announcement_style"),
                "content",
                ("enabled", "members_only"),
                "publish_start",
                "publish_end",
                "dismissal_type"],
        }),
    ]

    class Media:
        css = {
            'all': ('pinax/announcements/admin/admin.min.css',)
        }

    def save_model(self, request, obj, form, change):
        if not change:
            # When creating a new announcement, set the creator field.
            obj.creator = request.user
        obj.save()


class DismissalAdmin(admin.ModelAdmin):
    list_display = ("user", "announcement", "dismissed_at")

    def get_search_fields(self, request):
        User = get_user_model()
        if hasattr(User, "USERNAME_FIELD"):
            username_search = f"user__{User.USERNAME_FIELD}"
        else:
            username_search = "user__username"
        return (username_search, "announcement__title")


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Dismissal, DismissalAdmin)

