from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Promotion(models.Model):
    promotion_name = models.CharField(max_length=200)
    def __str__(self):
        return self.promotion_name

class Notes(models.Model):
    notes_value = models.FloatField(max_length=4)
    def __str__(self):
        return str(self.notes_value)

class Average(models.Model):
    average_value = models.FloatField(max_length=4)
    def __str__(self):
        return str(self.average_value)

class Classes(models.Model):
    classes_name = models.CharField(max_length=200)
    def __str__(self):
        return self.classes_name

class Student(models.Model):
    student_firstname = models.CharField(max_length=200)
    student_lastname = models.CharField(max_length=200)
    #student_birth = models.DateTimeField('birth_date')
    student_promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    student_notes = models.ManyToManyField(Notes)
    student_classes = models.ManyToManyField(Classes)
    student_average = models.ForeignKey(Average, on_delete=models.CASCADE)
    student_image = models.ImageField()

    def __str__(self) :
        return "{} {}, promotion {}, notes : {}, cours : {}, moyenne {}".format(self.student_firstname, self.student_lastname, self.student_promotion, self.student_notes, self.student_classes, self.student_average)