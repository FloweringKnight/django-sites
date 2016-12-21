from django.shortcuts import render
import os


def urls_second(request):
	context = {'dir': os.path.abspath('.')}
	return render(request, template_name='index.html', context=context)
