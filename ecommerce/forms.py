from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "form_full_name", "placeholder": "Your Fullname"}
            )
            )

    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "id": "form_email", "placeholder": "Your Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id": "form_content", "placeholder": "Write Something Here.."}))



    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email Has to be gmail.com")
        return email

    