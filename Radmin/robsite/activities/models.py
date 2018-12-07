from django.db import models
from datetime import date

class Activity(models.Model):
    activity_name = models.CharField(max_length = 200)
    activity_score = models.IntegerField()
    
    def get_name(self):
        return self.activity_name
		
    def get_score(self):
        return self.activity_score

    def rename(self, name):
        self.activity_name = name
    
    def set_score(self, score):
        self.activity_score = score
		
    def __str__(self):
        return " ".join((self.activity_name, str(self.activity_score)))
	

class RepeatedActivity(Activity):
    pass

	
class OneTimeActivity(Activity):
    activity_date = models.DateField()
	
    def get_date(self):
        return self.activity_date

    def set_date(self, date):
        self.activity_date = date
		
    def is_past(self):
        return date.today() > self.activity_date
	
    def __str__(self):
        return " ".join((self.activity_name, str(self.activity_score), str(self.activity_date)))

		
class Student(models.Model):
    GRADE_CHOICES = (("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"))
    student_name = models.CharField(max_length = 200)
    student_grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default="9")
    student_score = 0

    def add_score(self, score):
        self.student_score += score
		
    def __str__(self):
        return " ".join((self.student_name, self.student_grade, str(self.student_score)))
