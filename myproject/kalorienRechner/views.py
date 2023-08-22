from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from .forms import *
from django.shortcuts import redirect
from .models import Meal
from datetime import date as dt

# Create your views here.
def meal_list_today(request):
    meals = Meal.objects.filter(consumed_date__lte=timezone.now()).order_by('consumed_date').reverse()
    newMeals = []

    for meal in meals:
            if(meal.consumedToday()):
                newMeals.append(meal)

    return render(request, 'kalorienRechner/meal_list_today.html', {'meals': newMeals})

def meal_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    return render(request, 'kalorienRechner/meal_detail.html', {'meal': meal})

def meal_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.save()
            return redirect('meal_detail', pk=meal.pk)
    else:
        form = PostForm()
    return render(request, 'kalorienRechner/meal_new.html', {'form': form})

def meal_edit(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=meal)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.name = request.name
            meal.consumed_date = timezone.now()
            meal.calorie_count = request.calorie
            meal.save()
            return redirect('meal_detail', pk=meal.pk)
    else:
        form = PostForm(instance=meal)
    return render(request, 'kalorienRechner/meal_edit.html', {'form': form})

def meal_history_list(request):
    meals = Meal.objects.filter(consumed_date__lte=timezone.now()).order_by('consumed_date').reverse()
    newMeals = []

    date = request.POST.get('date', None)

    if date != None:
        dateTimeObj = datetime.strptime(request.POST['date'], "%Y-%m-%d")

        for meal in meals:
            if(meal.consumed_date.date() == dateTimeObj.date()):
                newMeals.append(meal)

        return render(request, 'kalorienRechner/meal_list.html', {'meals': newMeals})
    
    else:
        return render(request, 'kalorienRechner/meal_list.html', {'meals': meals})