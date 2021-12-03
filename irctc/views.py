from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import Trainn, SearchForm, BookingForm
from django.contrib.auth.models import User

def search(request):
    if request.method=='GET':
        return render(request, 'irctc/search.html', {'form':SearchForm()})
    else:
        try:
            form=SearchForm(request.POST)
            f=form.save(commit=True)
            f.save()
            print("added")
            return redirect('train')
        except ValueError:
            print("not added")
            return render(request, 'irctc/search.html', {'form':SearchForm})

def previous(request):
    user1 = Search.objects.filter()
    return render(request, 'irctc/previoustrip.html', {'user1': user1})


def train(request):
    user1=Train.objects.filter()
    return render(request, 'irctc/train.html', {'user1': user1})

def display(request,t):
    x=get_object_or_404(Train, pk=t)
    print("vantan")
    if request.method == "GET":
        form=Trainn(instance=x)
        print("gotit")
        return render(request, 'irctc/display.html', {'x':x, 'form':form})
    else:
        try:
            form=Trainn(instance=x)
            form.save()
            print("never gotit")
            return redirect('train')
        except ValueError:
            return render(request, 'irctc/display.html', {'x': x, 'form':form})


