from django import forms
from .models import About, MeetingReport

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        # specify field to be displayed from model here
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MeetingReportForm(forms.ModelForm):

    class Meta:
        model = MeetingReport
        fields = ['date', 'partners_name', 'moderator', 'city_nation', 'prayer_request', 'general_comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'input_classes'}),
            'prayer_request': forms.Textarea(attrs={'rows': 4, 'class': 'input_classes min-h-[100px]'}),
            'general_comment': forms.Textarea(attrs={'rows': 4, 'class': 'input_classes min-h-[100px]'}),
        }

        def __init__(self, *args, **kwargs):
            super(AboutForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'

