from django.urls import path, re_path

from . import views

app_name = 'robots_scraper'

urlpatterns = [
    # re_path(r'^(index)?$', views.index, name='index'),
    path('website', views.website, name='website'),
    path('test', views.test, name='test')
]
