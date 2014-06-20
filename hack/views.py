from django.shortcuts import (render, render_to_response, get_object_or_404)

# the homepage
def home(request):
	return render(request, 'homepage.html', {})

# add basic event information for a new event
def new_event(request):
	return render(request, 'new_event.html', {})

# the event pages
def event_page(request, event_id):
	context = {'event_id': event_id}
	return render(request, 'event.html', context)
