from telnetlib import SE
from django.contrib import admin
from .models import Content, Cluster, ServiceTag, Service, OrganizationTag, Organization, Event, Office, Newsletter, NewsletterCategory

# Register your models here.
admin.site.register(Content)
admin.site.register(Cluster)
admin.site.register(Office)
admin.site.register(ServiceTag)
admin.site.register(Service)
admin.site.register(OrganizationTag)
admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(NewsletterCategory)
admin.site.register(Newsletter)

