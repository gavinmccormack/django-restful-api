from django.shortcuts import render

def listings(request):
	context = {"events": ['a','b']}
	return render(request, 'index.html', context) 