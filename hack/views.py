from django.shortcuts import (render, render_to_response, get_object_or_404)
from models import *

class res_1:
    id = 1
    url = "a.com"

class res_2:
    id = 2
    url = "b.com"

class res_3:
    id = 3
    url = "c.com"

class dummyEvent:
    id = 5
    name = "How to Git",
    description = "A workshop on learning Git."
    resources = [res_1, res_2, res_3]
    recommendation_1 = res_1
    recommendation_2 = res_2
    recommendation_3 = res_3

# the homepage
def home(request):
    return render(request, 'homepage.html', {})

# add basic event information for a new event
def new_event(request):
    return render(request, 'new_event.html', {})

# the event pages
def event_page(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    colors1 = ["bg-teal", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
         "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
          "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange"]
    colors2 = ["bg-yellow","bg-violet", "bg-teal", "bg-cyan",   "bg-lightGreen","bg-orange",
         "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
          "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange"]
    colors3 = [ "bg-violet", "bg-cyan", "bg-amber", "bg-lightGreen","bg-teal", "bg-orange",
         "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
          "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange"]
    context = {'event': event, 'colors1':colors1, 'colors2':colors2, 'colors3':colors3}
    return render(request, 'event.html', context)

# the survey page
def update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event}
    return render(request, 'update.html', context)

def save_update(request, event_id):
    event_rating = int(request.POST['rating'])+1 # should be 1-10 but this is untested
    resources = []
    for k in request.POST.keys():
        if "resource" in k:
            resources.append(request.POST[k])
    selected_resources = resources
    # TODO: save into survey table
    # TODO: do ML stuff here
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event}
    return render(request, 'event.html', context)
    