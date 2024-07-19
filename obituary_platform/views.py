from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Obituary
from .forms import ObituaryForm

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Obituary submitted successfully!')
    else:
        form = ObituaryForm()
    return render(request, 'obituary_form.html')