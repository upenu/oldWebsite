from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.template import Context, Template
from django.forms import *
from django.core.serializers.json import DjangoJSONEncoder
import json, re
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

from interview.models import Question


def index(request):
    template = loader.get_template('website/interview.html')
    questions = Question.objects.all()
    context = RequestContext(request, {'questions':questions})
    return HttpResponse(template.render(context))

# def index(request):
#     latest_question_list = Question.objects.all()[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'website/interview.html', context)

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'website/interview/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


#Question.objects.all()

