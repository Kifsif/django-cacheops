from django.db import models


class General(models.Model):

    def __str__(self):
        return "General"

    class Meta:
        verbose_name = "General"
        verbose_name_plural = verbose_name
