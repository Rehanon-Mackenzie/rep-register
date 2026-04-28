from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Workout(models.Model):
    """
    Represents a workout entry logged by a user.
    Stores exercise details including weight, sets, rep and date.
    Links to Django's built-in user model via a foreign key.
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    exercise = models.CharField(max_length=100)
    weight = models.IntegerField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    @property
    def volume(self):
        """
        Calculates total volume as weight multiplied by sets and reps.
        """
        return self.weight * self.sets * self.reps

    def __str__(self):
        """
        Returns the exercise name as  the string representation.
        """
        return self.exercise
