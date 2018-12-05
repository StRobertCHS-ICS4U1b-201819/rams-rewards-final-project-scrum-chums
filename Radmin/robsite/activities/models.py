from django.db import models

class Activity(models.Model):
    activity_name = models.CharField(max_length = 200)
    activity_score = models.IntegerField()
    
    def __str__(self):
        return " ".join((self.activity_name, str(self.activity_score)))
   