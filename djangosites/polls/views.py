from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import *
# from django.template import RequestContext, loader


# Create your views here.
#def index(request):
#	return HttpResponse('HELLO WORLD ——form the polls\'homepage')


def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404('Fuck the number!')
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, template_name='polls/detail.html', context=context)


def results(request, question_id):
	response = "You are looking at the results of question %s"
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("You are voting on question %s" % question_id)


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 2	template = loader.get_template('polls/index.html')
# 2	context = RequestContext(request, {
# 2		'latest_question_list': latest_question_list,
# 2	})
# 2	return HttpResponse(template.render(context))
# 1	out_put = ', '.join([p.question_text for p in latest_question_list])
# 1	return HttpResponse(out_put)
	context = {'latest_question_list': latest_question_list}
	return render(request, template_name='polls/index.html', context=context)

