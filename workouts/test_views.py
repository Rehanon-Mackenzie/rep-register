from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Workout


class TestWorkoutViews(TestCase):
    """
    Tests for workout views including access control and CRUD operations.
    """

    def setUp(self):
        """
        Initialises a test user and sample workout to be
        used across the test cases
        """
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword", email="test@test.com"
        )
        self.workout = Workout.objects.create(
                user=self.user, exercise="squat", weight="25", sets="3",
                reps="10")

    def test_workout_page_loads_for_logged_in_user(self):
        """
        Checks that the workout index page returns a 200 status
        for an authenticated user
        """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse("workouts:index"))
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        """
        Checks that unauthenticated users are redirected away
        from protected pages
        """
        response = self.client.get(reverse("workouts:index"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)
        self.assertIn("/workouts/", response.url)

    def test_correct_template_used(self):
        """
        Verifies that the correct HTML template is
        used when rendering the workout page
        """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse("workouts:index"))
        self.assertTemplateUsed(response, "workouts/index.html")

    def test_edit_workout(self):
        """
        Tests that an existing workout
        can be successfully updated with new data
        """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(
            reverse("workouts:edit_workout", args=[self.workout.id]),
            {
                "exercise": "deadlift",
                "weight": 50,
                "sets": 4,
                "reps": 12,
            }
            )
        self.workout.refresh_from_db()
        self.assertEqual(self.workout.exercise, "deadlift")

    def test_delete_workout(self):
        """
        Tests that a workout is correctly removed
        from the database when deleted
        """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(
            reverse("workouts:delete_workout", args=[self.workout.id])
        )
        self.assertEqual(Workout.objects.count(), 0)
