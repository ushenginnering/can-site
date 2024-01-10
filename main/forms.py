from django import forms
from .models import About

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        # specify field to be displayed from model here
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'