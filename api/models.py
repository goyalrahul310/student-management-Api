from django.db import models

# Create your models here.
class Student(models.Model):
	Gender = (("F","female"),("M","male"),("U","undisclosed"))
	name = models.CharField(max_length = 100)
	roll = models.IntegerField()
	gender = models.CharField(max_length = 1,choices = Gender)
	Degree = models.CharField(max_length = 100)
	email  = models.EmailField()
	institute = models.ForeignKey("Institute",on_delete = models.CASCADE,null = True,blank = True)

class Institute(models.Model):
	category = (("H","highschool"),("C","college"))
	name = models.CharField(max_length = 200)
	type_ins = models.CharField(max_length = 1,choices = category)
    
    # def __str__(self):
    # 	return self.name