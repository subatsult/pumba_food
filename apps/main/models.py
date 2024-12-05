from django.db import models

# Create your models here.









class Aboust_us(models.Model):
    history = models.TextField(verbose_name='Our History')
    mission = models.TextField(verbose_name='Our Mission')


    def __str__(self):
        return self.mission

class Meta:
    verbose_name='About Us'
    verbose_name_plural='About us'