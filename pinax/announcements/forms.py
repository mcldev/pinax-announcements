from ckeditor.widgets import CKEditorWidget
from django import forms
from fontawesome.widgets import IconWidget

from .config import ANNOUNCEMENT_STYLES
from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': '100', }))
    announcement_style = forms.ChoiceField(required=False, choices=ANNOUNCEMENT_STYLES)
    content = forms.CharField(widget=CKEditorWidget(), required=False)
    enabled = forms.BooleanField(initial=True, required=False,)
    class Meta:
        model = Announcement
        fields = [
            "title",
            "content",
            "enabled",
            "announcement_style",
            "members_only",
            "dismissal_type",
            "publish_start",
            "publish_end"
        ]
