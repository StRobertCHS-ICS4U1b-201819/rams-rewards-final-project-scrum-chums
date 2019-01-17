from django.db import models
# if we ever decide to implement teacher class then we may want to create basic user class and have both inheriting from it 

class Student(models.Model):
    """
    class for student objects  ->  people are objects represented by numbers
    
    student_name    ->  name of student *may want to split into first and last later on for sorting and stuff
    student_grade   ->  grade of student
    student_score   ->  number of points student has 
    """
    GRADE_CHOICES = (("9", "9"), ("10", "10"), ("11", "11"), ("12", "12")) # This is kinda stupid may want to change the key later
    # IIRC the key is the one on the left
    student_name = models.CharField(max_length = 200) # Maybe some Indian names too long??
    student_grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default="9")
    student_score = models.IntegerField()
    student_id = models.CharField(max_length=50)
    student_pass = models.CharField(max_length=50)
    student_history = models.TextField()
    

    def __str__(self):
        return " ".join((self.student_name, self.student_grade, str(self.student_score)))
