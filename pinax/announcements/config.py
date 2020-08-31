from django.conf import settings


ANNOUNCEMENT_DEFAULT_STYLES = [
    ('', '----'),
    ('danger', 'danger'),
    ('warning', 'warning'),
    ('info', 'info'),
    ('success', 'success'),
]

ANNOUNCEMENT_STYLES = getattr(settings, 'PINAX_ANNOUNCEMENT_STYLES', ANNOUNCEMENT_DEFAULT_STYLES)
