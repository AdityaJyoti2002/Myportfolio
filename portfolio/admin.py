from django.contrib import admin
from .views import *
# from .models import About, Service, RecentWork, Client
# Register your models here.
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Recentwork)
admin.site.register(Client)
admin.site.register(Contact)

