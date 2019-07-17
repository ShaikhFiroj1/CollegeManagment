from django.db import models
from django.urls import reverse

# Create your models here.
class StudentList(models.Model):
    RollNo = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    test1 = models.IntegerField(blank=True, null=True)
    test2 = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['RollNo']

    def get_absolute_url(self):
        
        return reverse('home')