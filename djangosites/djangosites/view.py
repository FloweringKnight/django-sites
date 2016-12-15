from django.http import HttpResponse, Http404


def urls_second(request):
	return HttpResponse('Hello World')