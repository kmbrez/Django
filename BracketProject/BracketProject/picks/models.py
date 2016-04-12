from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name