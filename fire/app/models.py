from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()


class Discipline(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()


class Progress(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()
    athlete = models.CharField(max_length=100)


class Trainer(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()


class Contacts(models.Model):
    working_hours = models.CharField(max_length=20)
    telephones = models.IntegerField()
    mail = models.EmailField()
