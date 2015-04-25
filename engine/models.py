from django.db import models


class PlayerNation(models.Model):
    name = models.CharField(max_length=128, unique=True)
    color = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name
