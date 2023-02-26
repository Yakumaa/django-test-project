from django.shortcuts import render
from.models import Destination

# Create your views here.
def index(request):
    # dest3 = Destination()
    # dest3.name = 'Kathmandu'
    # dest3.desc = 'blah blah'
    # dest3.price = 100
    # dest3.img = '/static/images/kathmandu3.jpg'
    # # dest3.offer = True

    # dest2 = Destination()
    # dest2.name = 'Pokhara'
    # dest2.desc = ' more blah blah'
    # dest2.price = 200
    # dest2.img = '/static/images/pokhara.jpg'
    # # dest2.offer = True

    # dest1 = Destination()
    # dest1.name = 'Bhaktapur'
    # dest1.desc = 'more blah blah blah'
    # dest1.price = 300
    # dest1.img = '/static/images/bhaktapur.jpg'
    # # dest1.offer = True

    # dests = [dest3, dest2, dest1]

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

def contact(request):
    return render(request, 'contact.html')
