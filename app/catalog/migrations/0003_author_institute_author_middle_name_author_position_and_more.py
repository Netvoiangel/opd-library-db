# Generated by Django 4.2.13 on 2024-05-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_author_pdffile_direction_pdffile_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='institute',
            field=models.CharField(default='IPMEIT', max_length=100),
        ),
        migrations.AddField(
            model_name='author',
            name='middle_name',
            field=models.CharField(default='Ivanovich', max_length=100),
        ),
        migrations.AddField(
            model_name='author',
            name='position',
            field=models.CharField(default='scientist', max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='Ivan', max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='Ivanov', max_length=100),
        ),
    ]
