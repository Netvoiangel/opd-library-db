from django.shortcuts import render, get_object_or_404
from .models import PDFFile

def pdf_view(request, pdf_id):
    pdf = get_object_or_404(PDFFile, pk=pdf_id)
    return render(request, 'pdf_view.html', {'pdf': pdf})

def index(request):
    pdfs = PDFFile.objects.all()
    return render(request, 'index.html', {'pdfs': pdfs})
