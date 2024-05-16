from django.shortcuts import render
from libraryDataBase.models import Article

from django.http import HttpResponseRedirect
from .forms import DocumentForm

# Create your views here.

def index_page(request):
    all_articles = Article.objects.all()
    print(all_articles)

    return render(request, 'index.html')

def upload_pdf(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})