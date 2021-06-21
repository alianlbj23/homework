from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from django.http import HttpResponse
#from django.template import loader
from .models import Post, City
from datetime import datetime
from django.shortcuts import redirect
import random


def home(request):
    return render(request, 'home.html', locals())

def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())

def index(request):
	posts = Post.objects.all()
	myname = "曾裕翔"
	data = [i for i in range(1, 43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number = data[6]
	now = datetime.now()
	headMessage = "測試"
	return render(request, 'index.html', locals())

def showpost(request, id):
	try:
		post = Post.objects.get(id = id)
	except:
		return redirect('/')
	return render(request, "post.html", locals())


def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })