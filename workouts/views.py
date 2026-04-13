from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
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
            messages.add_message(request, messages.SUCCESS, 'Workout added!')
            return redirect('workouts:index')
    else:
        form = WorkoutForm()
    return render(request, 'workouts/add_workout.html', {'form': form})




@login_required
def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Workout edited!')
            return redirect('workouts:index')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/edit_workout.html', {'form': form})


@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == "POST":
        workout.delete()
        messages.add_message(request, messages.SUCCESS, 'Workout deleted!')
        return redirect('workouts:index')
    return redirect('workouts:index')
