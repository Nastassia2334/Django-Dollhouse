from django.db import models


# Create your models here.
class WarrantyReturn(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    name_description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name
