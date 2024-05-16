from django.db import models

# Create your models here.

from django.db import models

class Document(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')а

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)

    def __str__(self):
       return self.full_name

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    link = models.URLField()

    def __str__(self):
       return self.title

class MainTable(models.Model):
    #id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
      return self.title