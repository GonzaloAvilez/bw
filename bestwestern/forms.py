# coding: utf-8
from django import forms 


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        label='Name'
        )
    contact_email = forms.EmailField(
        required=True,
        label='Email'
        )
    phone = forms.CharField (
        required = False,
        label='Teléfono',
        )
    content = forms.CharField (
        required=True,
        widget=forms.Textarea,
        label='Inquietud'
        )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre',
        })
        self.fields['contact_email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Correo',
        })
        # self.fields['phone'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'Teléfono',
        # })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mensaje',
        })




