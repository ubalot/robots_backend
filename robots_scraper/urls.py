from django.urls import path, re_path

from . import views

app_name = 'robots_scraper'

urlpatterns = [
    # re_path(r'^(index)?$', views.index, name='index'),
    path('website', views.add_website, name='website'),
    path('websites_list', views.websites_list, name='websites_list'),
    path('test', views.test, name='test')
]
