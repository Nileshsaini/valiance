from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect


def plot(request):
	return render(request, 'plot.html', {})