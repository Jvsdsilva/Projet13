from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import admin
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from yoga.models import UploadImage, Events
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


# go to home
def index(request):
    logger.info('index', exc_info=True, extra={
        # Optionally pass a request and we'll grab any information we can
        'request': request,
    })
    user_logged = None
    user_logged = request.user.username

    all_uploads = UploadImage.objects.all()

    if user_logged == 'admin':
        return render(request, 'yoga/index_admin.html',
                      {'uploads': all_uploads})
    else:
        return render(request, 'yoga/index.html',
                      {'uploads': all_uploads})


def gimyoga(request):
    template = loader.get_template('yoga/gim_yoga.html')
    return HttpResponse(template.render(request=request))


def gigong(request):
    template = loader.get_template('yoga/gi_gong.html')
    return HttpResponse(template.render(request=request))


def professeur(request):
    template = loader.get_template('yoga/professeur.html')
    return HttpResponse(template.render(request=request))


def cours(request):
    template = loader.get_template('yoga/cours.html')
    return HttpResponse(template.render(request=request))


def contact(request):
    template = loader.get_template('yoga/contact.html')
    return HttpResponse(template.render(request=request))


def blog(request):
    user_logged = None
    user_logged = request.user.username

    all_events = Events.objects.all()

    if user_logged == 'admin':
        return render(request, 'yoga/blog_admin.html', {'event': all_events})

    else:
        return render(request, 'yoga/blog.html', {'event': all_events})


def addEvent(request):

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        newEvent = Events(
                title=request.POST['title'],
                text=request.POST['text'],
                thumb=uploaded_file_url
                )

        newEvent.save()
        return redirect('blog')
    else:
        if request.method == 'POST':
            newEvent = Events(
                    title=request.POST['title'],
                    text=request.POST['text']
                    )

            newEvent.save()
            return redirect('blog')
        else:
            return render(request, 'yoga/add_event.html')


# loged in
def login(request):
    template = loader.get_template('yoga/login.html')
    return HttpResponse(template.render(request=request))


# logout user
def logout(request):
    template = loader.get_template('yoga/index.html')
    return HttpResponse(template.render(request=request))


# Create new user
def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'yoga/signup.html', {'form': form})


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        newImage = UploadImage(
                 title=request.POST['title'],
                 thumb=uploaded_file_url
                 )

        newImage.save()
        return redirect('index')
    else:
        return render(request, 'yoga/simple_upload.html')
