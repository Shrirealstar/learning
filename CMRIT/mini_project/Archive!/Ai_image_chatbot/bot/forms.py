from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload an image')

class ChatForm(forms.Form):
    user_message = forms.CharField(
        label='Your Message', 
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40})
    )
