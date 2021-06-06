from django.shortcuts import redirect, render
from datetime import date
from django.contrib.auth.decorators import login_required

from .models import Business, Event, ImagePost, Neighbourhood, TextPost, Profile
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    current_neighbourhood = current_user.neighbourhood
    
    if request.method == 'POST':
        new_post_text_content = request.POST.get('content')
        if request.FILES['image']:
            new_post_image = request.FILES['image']
            new_image_post = ImagePost(user=current_user, neighbourhood=current_neighbourhood, text_content=new_post_text_content, image=new_post_image,)
            new_image_post.create_post()
            return redirect('Home')
            
        else:
            new_text_post = TextPost(user=current_user, neighbourhood=current_neighbourhood, text_content=new_post_text_content, )
            new_text_post.create_post()
            return redirect('/')
            
    all_text_posts = TextPost.get_neighbourhood_posts()
    all_image_posts = ImagePost.get_neighbourhood_posts()
    
    all_posts = dict()
    
    all_posts.update(all_text_posts)
    all_posts.update(all_image_posts)
    
    sorted_posts = sorted(all_posts.items(), key= lambda x: x['created_on'], reverse= True )
    
    all_events = Event.objects.all()
    
    todays_dates = date.today()
    upcoming_events = list()
    
    for event in all_events:
        if event.create_on < todays_dates:
            upcoming_events.append(event)
            
        
    title = 'Neighbourhood: Home'
    
    return render(request, 'index.html', {'title': title, 'posts': sorted_posts, 'events': upcoming_events})


@login_required(login_url='/accounts/login/')
def events(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    current_neighbourhood = current_user.neighbourhood
    
    if request.method == 'POST':
        new_event_title = request.POST.get('title')
        new_event_location = request.POST.get('location')
        new_event_date = request.POST.get('date')
        
        new_event = Event(title = new_event_title, location = new_event_location, date = new_event_date, neighbourhood = current_neighbourhood)
        new_event.create_event()  
        
        return redirect('/events')      
    
    all_events = Event.objects.filter(neighbourhood=current_neighbourhood).all()
    title = 'Neighbourhood: All Events'
    
    return render(request, 'events.html', {'title': title, 'events': all_events})
    
    
@login_required(login_url='/accounts/login/')
def upcoming_events(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    current_neighbourhood = current_user.neighbourhood
    
    all_events = Event.objects.filter(neighbourhood=current_neighbourhood).all()
    
    todays_date = date.today()
    upcoming_events = list()
    
    for event in all_events:
        if event.date > todays_date:
            upcoming_events.append(event)
    
    title = 'Neighbourhood: Upcoming Events'
    
    return render(request, 'events.html', {'title': title, 'events': upcoming_events})


@login_required(login_url='/accounts/login/')
def past_events(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    current_neighbourhood = current_user.neighbourhood
    
    all_events = Event.objects.filter(neighbourhood=current_neighbourhood).all()
    
    todays_date = date.today()
    past_events = list()
    
    for event in all_events:
        if event.date < todays_date:
            past_events.append(event)
    
    title = 'Neighbourhood: Past Events'
    
    return render(request, 'events.html', {'title': title, 'events': past_events})