from django.db import models

class Student(models.Model):
    GRADE_CHOICES = (("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"))
    student_name = models.CharField(max_length = 200)
    student_grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default="9")
    student_score = models.IntegerField()
		
    def __str__(self):
        return " ".join((self.student_name, self.student_grade, str(self.student_score)))
