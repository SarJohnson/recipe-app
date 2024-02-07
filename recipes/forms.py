from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

DIFFIC__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Intermediate'),
    ('#3', 'Hard'),
    ('#4', 'Expert')
)

class RecipeSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFIC__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)