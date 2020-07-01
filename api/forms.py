from django import forms
from api.models import Post


class AddPostForm(forms.Form):
    CHOICE = (
        ("BO", "BOAST"),
        ("RO", "ROAST")
    )
    choice = forms.ChoiceField(choices=CHOICE, label="Roast or Boast",
                               initial='', widget=forms.Select(), required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
