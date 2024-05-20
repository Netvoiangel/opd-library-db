from django.shortcuts import render, get_object_or_404, redirect
from .models import PDFFile, Author
from django.contrib.auth.decorators import login_required, user_passes_test

def pdf_view(request, pdf_id):
    pdf = get_object_or_404(PDFFile, pk=pdf_id)
    is_author = request.user.is_authenticated and hasattr(request.user, 'author')
    return render(request, 'pdf_view.html', {'pdf': pdf, 'is_author': is_author})

def is_author(user):
    return hasattr(user, 'author')

def index(request):
    pdfs = PDFFile.objects.all()
    is_author = request.user.is_authenticated and hasattr(request.user, 'author')
    return render(request, 'index.html', {'pdfs': pdfs, 'is_author': is_author})

@login_required
@user_passes_test(is_author)
def delete_pdf(request, pdf_id):
    pdf = get_object_or_404(PDFFile, pk=pdf_id)
    if request.method == 'POST':
        pdf.delete()
        return redirect('index')
    return render(request, 'confirm_delete.html', {'pdf': pdf})

@login_required
@user_passes_test(is_author)
def add_pdf(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        direction = request.POST.get('direction')
        pdf_file = request.FILES.get('pdf_file')
        author_ids = request.POST.getlist('authors')

        pdf = PDFFile(title=title, direction=direction, pdf=pdf_file)
        pdf.save()

        for author_id in author_ids:
            author = Author.objects.get(pk=author_id)
            pdf.authors.add(author)
            author.pdf_file_set.add(pdf)

        return redirect('index')
    else:
        authors = Author.objects.all()
        return render(request, 'add_pdf.html', {'authors': authors})
    
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})
