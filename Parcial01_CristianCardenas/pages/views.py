from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import TemplateView, ListView 
from django.views import View 
from django.http import HttpResponseRedirect 
from django.urls import reverse 
from django import forms 
from django.core.exceptions import ValidationError 
from .models import Flight 

# Create your views here.
class HomePageView(TemplateView):
 template_name = 'pages/home.html'

    
class FlightListView(ListView): 
    model = Flight 
    template_name = 'product_list.html' 
    context_object_name = 'flights'  # This will allow you to loop through 'products' in your template 
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Products - Online Store' 
        context['subtitle'] = 'List of products' 
        return context   

class FlightForm(forms.ModelForm):
    class Meta: 
        model = Flight 
        fields = ['name', 'flight_type', 'price'] 
 
    def clean_price(self): 
        price = self.cleaned_data.get('price') 
        if price is not None and price <= 0: 
            raise ValidationError('Price must be greater than zero.') 
        return price 
    
def flight_create(request):
    template_name = 'pages/register.html'

    def get(self, request):
        form = FlightForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(form)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)