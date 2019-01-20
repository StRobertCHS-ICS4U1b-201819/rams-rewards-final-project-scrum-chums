from django.db import models

class Activitie(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    points = models.IntegerField()
    
    def __str__(self):
        return self.title
    
