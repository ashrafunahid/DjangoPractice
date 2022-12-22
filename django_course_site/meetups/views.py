from django.shortcuts import render

# Create your views here.


def index(request):
    meetups = [
        {
            'title': "First Meetups", 
            'location': 'New York', 
            'slug': 'first-meetups'
        },
        {
            'title': "Second Meetups", 
            'location': 'Paris', 
            'slug': 'second-meetups'
        },
        {
            'title': "Third Meetups", 
            'location': 'Dhaka', 
            'slug': 'third-meetups'
        },
    ]
    return render(request, "meetups/index.html", {
        'show_meetups': True,
        'meetups': meetups,
    })

def meetup_details(request):
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is First Meetup',
    }
    return render(request, "meetups/meetup-detail.html", {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
