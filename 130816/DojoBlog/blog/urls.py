from django.conf.urls import url
from . import views

urlpatterns=[
            url(r'^$', views.showPosts, name='show_posts')
                ]