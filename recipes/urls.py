from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('recipes', views.recipes_list_page, name='recipes-list-page'),
    path('recipes/<int:recipe_id>', views.recipe_details_page,
         name='recipe-details-page')
]
