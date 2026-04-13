from django.urls import path # import path, similar to project's urls.py
from . import views # import views.py from the current directory

app_name = 'workouts'

urlpatterns = [
    path('', views.index, name='index'),
    path("add/", views.add_workout, name="add_workout"),
    path("edit/<int:workout_id>/", views.edit_workout, name="edit_workout"),
    path("delete/<int:workout_id>/", views.delete_workout, name="delete_workout"),
]
