from django.db import models

class Activitie(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    # points = models.DecimalField(max_digits = 10000, decimal_places = 0)
    
    def __str__(self):
        return self.title
    
