from django.test import TestCase
from .forms import WorkoutForm


class TestWorkoutForm(TestCase):

    def test_form_valid_data(self):
        form = WorkoutForm(data={
            "exercise": "squat",
            "weight": 25,
            "sets": 3,
            "reps": 10,
        })

        self.assertTrue(form.is_valid())

    def test_form_missing_fields(self):
        form = WorkoutForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("exercise", form.errors)
