from django.shortcuts import render

def home(request):
	context = {
		"words" : [
			"I",
			"am",
			"Paul",
			"Aranzamendez"
		],
		"source" : 'NLTLK',
		"version" : 1.5
	}
	return render(request, 'index.html', context)