from django.db import models
from engine.models import PlayerNation


class Region(models.Model):
    name = models.CharField(max_length=128, unique=True)
    owner = models.ForeignKey(PlayerNation, null=True, blank=True)
    has_supply_center = models.BooleanField()
    has_coast = models.BooleanField()
    is_neutral = models.BooleanField(default=False)
    is_ocean = models.BooleanField(default=False)
    neighbors = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __unicode__(self):
        return self.name
