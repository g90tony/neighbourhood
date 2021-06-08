from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='Home'),
    path('/events', views.events, name='All Events'),
    path('/events/upcoming', views.upcoming_events, name='Upcoming Events'),
    path('/events/past', views.past_events, name='Past Events'),
    path('/businesses', views.businesses, name='All Businesses'),
    path('/businesses/search', views.busines_search, name='Businesses Search'),
]