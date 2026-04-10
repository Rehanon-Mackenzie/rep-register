from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout
from .forms import WorkoutForm

# Create your views here.

@login_required
def index(request):
    workouts = Workout.objects.filter(user=request.user)
   
    context = {
        "workouts": workouts
    }
    return render(request,"workouts/index.html", context)

@login_required
def add_workout(request):
    if request.method== "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
    else:
        form = WorkoutForm()
    return render(request, "workouts/add_workout.html", {"form": form})
