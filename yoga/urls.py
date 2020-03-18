from django.conf.urls import url
from django.urls import path
from .import views  # import views so we can use them in urls.
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$', views.index),
    url(r'^index', views.index, name="index"),
    url(r'^login/$', LoginView.as_view(template_name='yoga/login.html'),
        name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='yoga/index.html'),
        name='logout'),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^gimyoga', views.gimyoga, name="gimyoga"),
    url(r'^gigong', views.gigong, name="gigong"),
    url(r'^professeur', views.professeur, name="professeur"),
    url(r'^cours', views.cours, name="cours"),
    url(r'^contact', views.contact, name="contact"),
    url(r'^blog', views.blog, name="blog"),
    url(r'^upload', views.upload, name="upload"),
    url(r'^addEvent', views.addEvent, name="addEvent"),
]
