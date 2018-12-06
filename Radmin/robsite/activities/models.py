from django.db import models

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
	
	