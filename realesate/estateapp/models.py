from django.db import models

class Register(models.Model):
    # Define your model fields here
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Age = models.IntegerField()

    # Add any additional fields as needed

    def __str__(self):
        return self.Name
