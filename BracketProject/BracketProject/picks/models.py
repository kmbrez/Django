from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Team(models.Model):
    region = models.ForeignKey(Region, default=0)
    name = models.CharField(max_length=255)
    seed = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name