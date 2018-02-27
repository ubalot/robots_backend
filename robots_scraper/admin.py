from django.contrib import admin

# Register your models here.
from robots_scraper.models import WebSite, UserAgent, Rule

admin.site.register(WebSite)
admin.site.register(UserAgent)
admin.site.register(Rule)
