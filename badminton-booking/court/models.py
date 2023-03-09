from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.postgres.fields import ArrayField
from user.models import User

# Create your models here.


class Court(TimeStampedModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

    class Meta:
        verbose_name = 'AddCourt'
        verbose_name_plural = 'AddCourt'
        ordering = ['name']

    def __str__(self):
        return self.name


class Booking(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    court = models.ForeignKey('Court', on_delete=models.CASCADE, related_name="booking")
    date = models.DateField()
    timeslot = ArrayField(models.CharField(max_length=255), blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Booking"
        ordering = ['price']

    def __str__(self):
        return f'{self.user.email} - {str(self.price)}'
