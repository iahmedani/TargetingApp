# comparer/forms.py

from django import forms

class ExcelCompareForm(forms.Form):
    first_document = forms.FileField(
        label='First Excel Document',
        required=True,
        help_text='Upload the first Excel file for comparison.',
         widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx,.xls'
        })
    )
    second_document = forms.FileField(
        label='Second Excel Document',
        required=True,
        help_text='Upload the second Excel file to compare against the first.',
         widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx,.xls'
        })
    )
