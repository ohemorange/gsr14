from django.shortcuts import (render, render_to_response, get_object_or_404)
from models import *
import sqlite3,sys
import os
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

colors1 = ["bg-teal", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
         "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
          "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange"]
colors2 = ["bg-yellow","bg-violet", "bg-teal", "bg-cyan",   "bg-lightGreen","bg-orange",
     "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
      "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange"]
colors3 = [ "bg-violet", "bg-cyan", "bg-amber", "bg-lightGreen","bg-teal", "bg-orange",
     "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange",
      "bg-cyan", "bg-amber", "bg-lightGreen", "bg-violet", "bg-teal", "bg-orange"]

# the homepage
def home(request):
    conn = None
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    events = []
    for f in files:
        print f
    try:
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute('SELECT Name, id FROM hack_event')
        rows = cur.fetchall()
        print rows
        for (name, id) in rows:
            d = {"name":name, "id":id}
            events.append(d)
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        conn.close() 	
    print events
    context = {'events': events}
    return render(request, 'homepage.html', context)

# add basic event information for a new event
def new_event(request):
    return render(request, 'new_event.html', {})

# save basic event info and load event page or update page
def create_event(request):
    event_name = request.POST["event_name"]
    event_description = request.POST["description"]
    event = Event(name=event_name, description=event_description)
    event.save()
    action = request.POST["save"]
    if action == "Save":
        context = {'event': event, 'colors1':colors1, 'colors2':colors2, 'colors3':colors3}
        return render(request, 'event.html', context)
    else:
        context = {'event': event}
        return render(request, 'update.html', context)

# the event pages
def event_page(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event, 'colors1':colors1, 'colors2':colors2, 'colors3':colors3}
    return render(request, 'event.html', context)

# the survey page
def update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event}
    return render(request, 'update.html', context)

def save_update(request, event_id):
    cancel = request.POST['cancel']
    if cancel == "Cancel":
        event = get_object_or_404(Event, pk=event_id)
        context = {'event': event}
        return render(request, 'event.html', context)
    event_rating = request.POST['rating']
    if event_rating != "not_run":
        event_rating = int(event_rating)+1 # should be 1-10 but this is untested
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
    
def create_resource(request, event_id):
    resource_name = request.POST["resource_name"]
    resource_link = request.POST["resource_link"]
    resource_description = request.POST["resource_description"]
    resource = Resource(name=resource_name, description=resource_description, link=resource_link)
    resource.save()
    event = get_object_or_404(Event, pk=event_id)
    event.resources.add(resource)
    event.save()
    context = {'event': event}
    return render(request, 'update.html', context)
    