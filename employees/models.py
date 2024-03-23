from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()
    department=models.CharField(max_length=200)
    email=models.EmailField()


    def __str__(self):
        return self.name