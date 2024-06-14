from django.db import models

class StudentModel(models.Model):

    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50,null=True)
    student_address = models.TextField()
    student_department = models.CharField(max_length=50, null=True)
    student_image = models.ImageField(upload_to='images/', null=True)
