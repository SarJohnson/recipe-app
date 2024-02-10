from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Recipe
from .forms import RecipeSearchForm
from .utils import get_chart
import pandas as pd

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

def home(request):
    return render(request, 'recipes/home.html')

def stories(request):
    return render(request, 'recipes/stories.html')

def records(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    recipe_diff = None
    chart= None
    qs = None
    if request.method =='POST':
        recipe_diff = request.POST.get('recipe_diff')
        chart_type = request.POST.get('chart_type')
        if recipe_diff == '#1':
            recipe_diff = 'Easy'
        if recipe_diff == '#2':
            recipe_diff = 'Intermediate'
        if recipe_diff == '#3':
            recipe_diff = 'Hard'
        if recipe_diff == '#4':
            recipe_diff = 'Expert'
        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calc_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)
        qs = qs.filter(id__in=id_searched)
        if qs:
            recipes_df=pd.DataFrame(qs.values())
            chart=get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)
            recipes_df=recipes_df.to_html()
    context={
        'form': form,
        'recipes_df': recipes_df,
        'recipe_diff': recipe_diff,
        'chart': chart,
        'qs': qs,
    }
    return render(request, 'recipes/records.html', context)