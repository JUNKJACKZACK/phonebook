from django.shortcuts import render
from .models import Contact

# Create your views here
def index(request):
    current_phonebook = Contact.objects.all()
    context = {
        'phonebook': current_phonebook
    }
    return render(request, 'phonebook/index.html', context)