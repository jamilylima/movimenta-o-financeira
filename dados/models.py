from django.db import models

class Dados(models.Model):
    file  = models.FileField(upload_to='files/')

