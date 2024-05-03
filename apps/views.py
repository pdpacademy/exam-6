import profile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from apps.form import RegisterModelForm
from apps.models import Contact


# class ContactTemplateView(ListView):
#     template_name = "apps/index.html"

def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'apps/index.html', context)

class RegisterTemplateView(CreateView):
    template_name = "apps/register.html"
    form_class = RegisterModelForm
    success_url = "/register"