from django.urls import path

from . import views

# since name argument is defined here, 
# we dont have to be too specific with the url paths in the templates files

# to properly identify which app this view belongs to, add the app name
app_name = "polls"
# this is for the last tutorial 4
# changed from question_id to pk for 2nd and 3rd patterns since using the generic view to replace detail and results views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('owner', views.owner, name='owner'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

'''
this is for the first two tutorials
urlpatterns = [
    path("", views.index, name="index"),
    path('owner', views.owner, name='owner'),
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
'''