from django.db import models

class Activity(models.Model):
    activity_name = models.CharField(max_length = 200)
    activity_score = models.IntegerField()
    activity_date = models.DateField()
    # '%Y-%m-%d'      '2006-10-25'
    # '%m/%d/%Y'      '10/25/2006'
    # '%m/%d/%y'      '10/25/06'
    
    def __str__(self):
        return self.activity_name
   