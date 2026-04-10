from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Workout(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    exercise = models.CharField(max_length=100)
    weight = models.IntegerField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    @property
    def volume(self):
        return self.weight * self.sets * self.reps

    def __str__(self):
        return self.exercise
