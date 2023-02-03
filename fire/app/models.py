from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид спорта'


class Discipline(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дисциплина'


class Progress(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()
    athlete = models.CharField(max_length=100)

    def __str__(self):
        return self.athlete

    class Meta:
        verbose_name = 'Достижения'


class Trainer(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'


class Contacts(models.Model):
    working_hours = models.CharField(max_length=20)
    telephones = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return 'Контактные данные'

    class Meta:
        verbose_name = 'Контакты'
