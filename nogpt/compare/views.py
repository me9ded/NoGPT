from django.shortcuts import render
from . import forms

def create_form(request):
    form=forms.CreateForm()
    return render(request,'compare.html',{ 'form': form})

