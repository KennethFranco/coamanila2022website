from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.mail import EmailMessage, BadHeaderError
from django.conf import settings
from .models import Content, Newsletter, Organization, Event, Cluster, NewsletterCategory, ServiceTag, Service, Office
import datetime
# Create your views here.

def base(request):
    return render(request, "base.html")

def contactUs(request):
    if(request.method=="POST"):
        name = request.POST.get('name')
        fromEmail = request.POST.get('fromEmail')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        if subject and msg and fromEmail:
            email = EmailMessage(
                    subject, 
                    "From "+ name + ",\n" + msg,
                    settings.EMAIL_HOST_USER, 
                    [settings.EMAIL_HOST_USER],
                    reply_to = [fromEmail]
            )
            context = {
                "message": email.send(fail_silently=False),
                "prevName":name,
                "prevFromEmail": fromEmail,
                "prevSubj": subject,
                "prevMsg": msg,
            }
            return render(request, "contactUs.html", context)
    else:
        return render(request, "contactUs.html")

def home(request):
    today = datetime.date.today()
    currentMonth = today.strftime('%B')
    val1 = 0
    event = Event.objects.filter(start_date__month = today.month).order_by("start_date")
    event2 = Event.objects.filter(~Q(start_date__month = today.month) & Q(end_date__month = today.month)).order_by("end_date")
    event3 = event2 | event
    context = {
        "event": event3,
        "newsletter": Newsletter.objects.all().order_by("date").reverse(),
        "currentMonth": currentMonth,
        "val1": val1,
        "hometitle": Content.objects.get(id=8),
        "homedescription": Content.objects.get(id=3),
        'services': Service.objects.all().order_by("name"),
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "aboutUsVision": Content.objects.get(id=4),
        "aboutUsMission": Content.objects.get(id =5),
        "aboutUsOandC": Content.objects.get(id =6),
        "aboutUsDescription": Content.objects.get(id=7),
        "clusters": Cluster.objects.all().order_by("name"),
        "offices": Office.objects.all().order_by("order_on_website"),
    }
    
    return render(request, "about.html", context)

def organizations(request):
    context = {
        "organization": Organization.objects.all().order_by("name"),
        "event": Event.objects.all(),
        "cluster": Cluster.objects.all().order_by("name"),
    }
    return render(request, "organizations.html", context)
    
def indivorg(request,pk):
    lia = get_object_or_404(Organization, pk=pk)
    nameOfOrg = lia.abbreviation
    context = {
        "lia" : lia,
        "nameOfOrg": nameOfOrg,
        "event": Event.objects.filter(organization = pk).order_by("start_date"),
    }
    return render(request, "indivorg.html", context)

def newsletters(request):
    context  = {
        "newsletter": Newsletter.objects.all().order_by("date").reverse(),
        "newsletterOldest": Newsletter.objects.all().order_by("date"),
        "categories": NewsletterCategory.objects.all().order_by("title"),
    }
    return render(request, "newsletters.html", context)

def indivnewsletter(request,pk):
    lia = get_object_or_404(Newsletter, pk=pk)
    context = {
        "lia" : lia,
    }   
    return render(request, "indivnewsletter.html", context)

def articlepost(request):
    return render(request, "articlepost.html")

def services(request):
    context = {
        "services": Service.objects.all().order_by("name"),
        "serviceTags": ServiceTag.objects.all().order_by("title"),
    }
    return render(request, "services.html", context)
