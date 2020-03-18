from django.contrib import admin

# Register your models here.
from yoga.models import UploadImage
from yoga.models import Events

admin.site.register(UploadImage)
admin.site.register(Events)
