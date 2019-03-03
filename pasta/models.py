from django.db import models


class PastaType(models.Model):
    name = models.CharField(verbose_name='Pasta Name', max_length=50, null=False, blank=True, unique=True)
