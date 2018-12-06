from django.db import models
from datetime import date

class Activity(models.Model):
    activity_name = models.CharField(max_length = 200)
    activity_score = models.IntegerField()
    
    def get_name(self):
        return self.activity_name
		
    def get_score(self):
        return self.activity_score
		
    def str_score(self):
        return str(self.activity_score)
	
    def __str__(self):
        return " ".join((self.activity_name, str(self.activity_score)))
	
	
class OneTimeActivity(Activity):
    activity_date = models.DateField()
	
    def get_date(self):
        return self.activity_date
		
    def is_past(self):
        return date.today() > self.activity_date
	
    def __str__(self):
        return " ".join((self.activity_name, str(self.activity_score), str(self.activity_date)))