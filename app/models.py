from django.db import models
from django.contrib.auth.models import User

class Mahalla(models.Model):
    nomi = models.CharField(max_length=100)
    manzil = models.TextField()
    tashkil_qilgan_sana = models.DateField()
    fuqaro_soni = models.IntegerField()

    def __str__(self):
        return self.nomi

class EnergiyaSarfi(models.Model):
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    oy = models.CharField(max_length=20, choices=[
        ('Yanvar', 'Yanvar'), ('Fevral', 'Fevral'), ('Mart', 'Mart'),
        ('Aprel', 'Aprel'), ('May', 'May'), ('Iyun', 'Iyun'),
        ('Iyul', 'Iyul'), ('Avgust', 'Avgust'), ('Sentabr', 'Sentabr'),
        ('Oktabr', 'Oktabr'), ('Noyabr', 'Noyabr'), ('Dekabr', 'Dekabr')
    ])
    yil = models.IntegerField()
    elektr_kVt = models.FloatField()
    gaz_m3 = models.FloatField()
    suv_m3 = models.FloatField()
    qoʻshilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mahalla.nomi} - {self.oy} {self.yil}"


class Tavsiya(models.Model):
    name = models.CharField(max_length=26)
    text = models.TextField()

    def __str__(self):
        return self.name
    