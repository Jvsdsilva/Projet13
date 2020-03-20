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
        logger.info("admin user")
        return render(request, 'yoga/index_admin.html',
                      {'uploads': all_uploads})
    else:
        return render(request, 'yoga/index.html',
                      {'uploads': all_uploads})


# gym-yoga
def gimyoga(request):
    logger.info("page gim-yoga")
    template = loader.get_template('yoga/gim_yoga.html')
    return HttpResponse(template.render(request=request))


# gi-gong
def gigong(request):
    logger.info("page gi-gong")
    template = loader.get_template('yoga/gi_gong.html')
    return HttpResponse(template.render(request=request))


# teacher
def professeur(request):
    logger.info("page professeur")
    template = loader.get_template('yoga/professeur.html')
    return HttpResponse(template.render(request=request))


# schedule
def cours(request):
    logger.info("page cours")
    template = loader.get_template('yoga/cours.html')
    return HttpResponse(template.render(request=request))


# contact
def contact(request):
    logger.info("page contact")
    template = loader.get_template('yoga/contact.html')
    return HttpResponse(template.render(request=request))


# Event page
def blog(request):
    logger.info("page events")
    user_logged = None
    user_logged = request.user.username

    try:
        # get all events
        all_events = Events.objects.all()

        logger.info('get events', exc_info=True, extra={
            # Optionally pass a request and we'll grab any information we can
            'request': all_events,
        })
    except Exception:
        logging.exception(
            "We get some problems with request events")

    if user_logged == 'admin':
        logger.info("admin user")
        return render(request, 'yoga/blog_admin.html', {'event': all_events})

    else:
        return render(request, 'yoga/blog.html', {'event': all_events})


# add new Event
def addEvent(request):

    if request.method == 'POST' and request.FILES['myfile']:
        try:
            # get file
            myfile = request.FILES['myfile']

            logger.info('get file', exc_info=True,
                        extra={'request': myfile, }
                        )
        except Exception:
            logging.exception(
                "We get some problems with request file events")

        try:
            # get file
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)

            logger.info('get file', exc_info=True, extra={
                        'request': filename, })
        except Exception:
            logging.exception(
                "We get some problems with filename")

        try:
            # upload image
            uploaded_file_url = fs.url(filename)

            logger.info('upload image events', exc_info=True, extra={
                        'request': uploaded_file_url,
            })
        except Exception:
            logging.exception(
                "We get some problems with upload events image")

        newEvent = Events(
                title=request.POST['title'],
                text=request.POST['text'],
                thumb=uploaded_file_url
                )

        newEvent.save()
        return redirect('blog')
    else:
        logger.info("event view")
        return render(request, 'yoga/add_event.html')


# loged in
def login(request):
    logger.info("page login")
    template = loader.get_template('yoga/login.html')
    return HttpResponse(template.render(request=request))


# logout user
def logout(request):
    logger.info("page logout")
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


# Uplod new image
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:

        try:
            # get image
            myfile = request.FILES['myfile']

            logger.info('get file', exc_info=True,
                        extra={'request': myfile, }
                        )
        except Exception:
            logging.exception(
                "We get some problems with request image")

        try:
            # get image name
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)

            logger.info('get file', exc_info=True, extra={
                        'request': filename, })
        except Exception:
            logging.exception(
                "We get some problems with filename upload")

        try:
            # upload image
            uploaded_file_url = fs.url(filename)

            logger.info('upload image', exc_info=True, extra={
                        'request': uploaded_file_url,
            })
        except Exception:
            logging.exception(
                "We get some problems with upload image")

        newImage = UploadImage(
                 title=request.POST['title'],
                 thumb=uploaded_file_url
                 )

        newImage.save()
        return redirect('index')
    else:
        logger.info("page simple_upload")
        return render(request, 'yoga/simple_upload.html')
