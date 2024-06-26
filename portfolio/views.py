from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About, Service, Recentwork, Client, Contact

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = Recentwork.objects.all()
        context['clients'] = Client.objects.all()
        return context

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = Contact(name=name, Email=email, subject=subject, message=message)
        contact.save()
        return render(request, "index.html", {"name": name, "email": email, "subject":subject, "message":message})

    return render(request, "index.html")
