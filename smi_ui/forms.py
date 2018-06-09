from django.forms import forms, ClearableFileInput


class SignalForm(forms.Form):
    wav_file = forms.FileField(
        label='wav file',
        required=True,
        widget=ClearableFileInput(
            attrs={
                'style': 'display:none;',
                'class': 'wav_file'
            }
        )
    )