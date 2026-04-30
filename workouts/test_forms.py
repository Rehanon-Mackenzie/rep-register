from django.test import TestCase
from .forms import WorkoutForm


class TestWorkoutForm(TestCase):
    """
    Tests for the WorkoutForm validation with valid and missing data.
    """
    def test_form_valid_data(self):
        """
        Tests that the workout form is valid all required fields are provided
        """
        form = WorkoutForm(data={
            "exercise": "squat",
            "weight": 25,
            "sets": 3,
            "reps": 10,
        })

        self.assertTrue(form.is_valid())

    def test_form_missing_fields(self):
        """
        Tests that the workout form fails validation when
        required fields are missing
        """
        form = WorkoutForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("exercise", form.errors)
