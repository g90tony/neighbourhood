from django.shortcuts import redirect, render
from datetime import date
from django.contrib.auth.decorators import login_required

from .models import Business, Contact, Event, ImagePost, Neighbourhood, TextPost, Profile
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
    
    return render(request, 'events.html', {'title': title, 'events': past_events}) @login_required(login_url='/accounts/login/')



@login_required(login_url='/accounts/login/')
def businesses(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    current_neighbourhood = current_user.neighbourhood
    
    if request.method == 'POST':
        new_business_name = request.POST.get('business_name')
        new_user = current_user
        new_neighborhood = current_neighbourhood
        new_business_email = request.POST.get('business_email')
        
        new_business = Business(business_name = new_business_name, user = new_user, neighborhood = new_neighborhood, business_email = new_business_email)
        new_business.create_business()
        
        return redirect('/businesses')      
    
    all_businesses = Business.objects.filter(neighbourhood=current_neighbourhood).all()
    title = 'Neighbourhood: All Businesses'
    
    return render(request, 'businesses.html', {'title': title, 'businesses': all_businesses})
    



@login_required(login_url='/accounts/login/')
def busines_search(request, search_query):
    current_user = Profile.objects.filter(user = request.user).first()
    current_neighbourhood = current_user.neighbourhood
    
    if request.method is 'POST':
        query_results = Business.objects.filter(business_name = search_query, neighbourhood=current_neighbourhood).all()
        
        title= 'Neighbourhood: Business Search Results'
        
        return render(request, 'business_search.html', {'title': title, "results": query_results})
    
    return redirect('/businesses')

@login_required(login_url='/accounts/login/')
def contacts(request):
    
    current_user = Profile.objects.filter(user = request.user).first()
    current_neighbourhood = current_user.neighbourhood
    
    if request.method == 'POST':
        new_contact_name = request.POST.get('contact_name')
        new_neighborhood = current_neighbourhood
        new_contact_email = request.POST.get('contact_email')
        new_contact_phone_number = request.POST.get('contact_pnumber')
        
        new_business = Contact(name = new_contact_name,  neighborhood = new_neighborhood, email = new_contact_email, phone_number=new_contact_phone_number)
        new_business.create_business()
        
        return redirect('/businesses')      
    
    all_businesses = Business.objects.filter(neighbourhood=current_neighbourhood).all()
    title = 'Neighbourhood: All Businesses'
    
    return render(request, 'businesses.html', {'title': title, 'businesses': all_businesses})
    