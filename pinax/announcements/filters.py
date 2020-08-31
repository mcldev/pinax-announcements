from django.contrib import admin
from django.utils import timezone
from django.db.models import Q


# https://books.agiliq.com/projects/django-admin-cookbook/en/latest/filtering_calculated_fields.html
class IsEnabledFilter(admin.SimpleListFilter):
    title = 'Is Enabled'
    parameter_name = 'is_enabled'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(publish_start__lte=timezone.now()
                                   ).filter(Q(publish_end__isnull=True) | Q(publish_end__gt=timezone.now())
                                   ).filter(enabled=True)
        elif value == 'No':
            return queryset.filter(Q(publish_start__gt=timezone.now()) |
                                   Q(publish_end__lt=timezone.now()) |
                                   Q(enabled=False))
        return queryset
