from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Topic_name


class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    Email =models.EmailField(default='kalyansinha04@gmail.com')
    

    def __str__(self):
        return self.name

class AcessRocord(models.Model):
    date=models.DateField()
    author=models.CharField(max_length=100)
    
    def __str__(self):
        return self.author