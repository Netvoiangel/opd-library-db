from django import forms

class DocumentForm(forms.Form):
    pdf_file = forms.FileField(upload_to='pdfs/')
