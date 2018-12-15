from django.db import models

class Activitie(models.Model):
    """
    General class for activities *may want to make subclasses later on
    
    title  ->  activity name
    body   ->  general description
    points ->  points given by activity
    date   ->  date of activity *may make subclass exclusive later- only for fixed time events
    """
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    points = models.IntegerField()
    
    def __str__(self):
        return self.title
    
