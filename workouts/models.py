from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    """
   Stores a single workout entry for a logged-in user,
   related to :model:`auth.User`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
