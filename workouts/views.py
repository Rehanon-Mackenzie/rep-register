from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import WorkoutForm

# Create your views here.

@login_required
def index(request):
    workouts = Workout.objects.filter(user=request.user)
    
    context = {
        "workouts": workouts
    }
    return render(request,"workouts/index.html", context)