# Generated by Django 4.2.7 on 2023-12-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_webpage_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='Email',
            field=models.EmailField(default='kalyansinha04@gmail.com', max_length=254),
        ),
    ]