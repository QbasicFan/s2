
from django.db import models
from .thingsList import color

# Create your models here.



class front(models.Model):
    title = models.CharField(max_length=200)

    text1 = models.CharField(max_length=200)
    subText1 = models.CharField(max_length=200)

    text2 = models.CharField(max_length=200)
    subText2 = models.CharField(max_length=200)

    bgImage1 = models.ImageField(upload_to='static/img/')
    bgImage2 = models.ImageField(upload_to='static/img/')

    contactBGC = models.CharField(max_length=100 , choices=color)


    def __str__(self):
        return self.title


class section1(models.Model):
    title = models.CharField(max_length=200)

    text = models.TextField()
    linkName = models.CharField(max_length=200)

    image = models.ImageField(upload_to='static/img/')

    contactBGC = models.CharField(max_length=100 , choices=color)



    def __str__(self):
        return self.title


class section2(models.Model):
    title = models.CharField(max_length=200)

    text1 = models.CharField(max_length=200)
    subText1 = models.CharField(max_length=200)

    text2 = models.CharField(max_length=200)
    subText2 = models.CharField(max_length=200)

    image = models.ImageField(upload_to='static/img/')

    contactBGC = models.CharField(max_length=400 , choices=color)


    def __str__(self):
        return self.title





