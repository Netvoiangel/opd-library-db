from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100, default='Ivan')
    last_name = models.CharField(max_length=100, default='Ivanov')
    middle_name = models.CharField(max_length=100, default='Ivanovich')  # Отчество
    position = models.CharField(max_length=100, default='scientist')  # Должность
    institute = models.CharField(max_length=100, default='IPMEIT')  # Институт

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

class PDFFile(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    direction = models.CharField(max_length=100, default='common')  
    authors = models.ManyToManyField(Author)  

    def __str__(self):
        return self.title