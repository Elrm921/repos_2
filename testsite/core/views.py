from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EditForm, RegistrationForm
from .models import data
from datetime import datetime

# Base actions

def index(request):
    i = data.objects.order_by('-pub_date')
    return render(request, 'core/index.html', context={"items": i})

def detail(request, item_id):
    i = data.objects.filter(id=item_id)
    return render(request, 'core/detail.html', context={"item": i[0]})
    
def create_user(request):    
    if request.method == 'POST':
        d = request.POST.copy()
        new_user = User.objects.create_user(username=d.get('username'),
                                            email=d.get('email'),
                                            password=d.get('password'))
        new_user.save()
        return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()      
        return render(request, 'core/reg.html', context={'form': form})        


# User specific actions        

def edit(request, item_id):
    i = data.objects.filter(id=item_id)
    if request.method == 'POST':
        d = request.POST.copy()
        i.update(ad_title=d.get('ad_title'),
                 ad_text=d.get('ad_text'))
        return HttpResponseRedirect('/')
    else:
        form = EditForm(initial={'ad_title': i.values_list('ad_title', flat=True)[0],
                                 'ad_text': i.values_list('ad_text', flat=True)[0]})
        return render(request, 'core/edit.html', context={'form': form})
    
    
def delete(request, item_id):
    i = data.objects.filter(id=item_id)
    i.delete()
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def create_entry(request):
    if request.method == 'POST':
        d = request.POST.copy()
        data.objects.create(author=request.user,
                            pub_date = datetime.now(),
                            ad_title=d.get('ad_title'),
                            ad_text=d.get('ad_text'))
        return HttpResponseRedirect('/')
    else:
        form = EditForm()      
        return render(request, 'core/new.html', context={'form': form})    
