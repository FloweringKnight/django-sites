from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Question, Choice
# from django.template import RequestContext, loader


# Create your views here.
# def index(request):
#	 return HttpResponse('HELLO WORLD ——form the polls\'homepage')


def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404('Fuck the number!')
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, template_name='polls/detail.html', context=context)


def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')
# 2	template = loader.get_template('polls/index.html')
# 2	context = RequestContext(request, {
# 2		'latest_question_list': latest_question_list,
# 2	})
# 2	return HttpResponse(template.render(context))
# 1	out_put = ', '.join([p.question_text for p in latest_question_list])
# 1	return HttpResponse(out_put)
	context = {'latest_question_list': latest_question_list}
	return render(request, template_name='polls/index.html', context=context)


def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form
		return render(request, template_name='polls/detail.html', context={
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Alaways return on HttpResponseRedirect after successfully dealing with POST data
		# This prevent data from being posted twice if a user hits the Back button
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'lastest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_time')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
