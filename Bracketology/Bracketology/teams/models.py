from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    seed = models.IntegerField(default=0)


    def __str__(self):
        return self.name