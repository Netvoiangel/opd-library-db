from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, default='Ivan')
    last_name = models.CharField(max_length=100, default='Ivanov')
    middle_name = models.CharField(max_length=100, default='Ivanovich')  
    position = models.CharField(max_length=100, default='scientist')  
    institute = models.CharField(max_length=100, default='IPMEIT') 
    pdf_files = models.ManyToManyField('PDFFile', related_name='author_set', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
@receiver(post_save, sender=User)
def create_user_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_author(sender, instance, **kwargs):
    instance.author.save()

class PDFFile(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    direction = models.CharField(max_length=100, default='common')  
    authors = models.ManyToManyField(Author, related_name='pdf_file_set', blank=True)
    
    def __str__(self):
        return self.title