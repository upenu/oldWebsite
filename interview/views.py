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
    template = loader.get_template('interview/interview.html')
    questions = Question.objects.all()
    categories = {question.category for question in questions}
    sidebar_elems = [{"link": "#", "text": category} for category in categories]
    context = RequestContext(request, {'questions':questions, 'sidebar': {'title': "Categories", 'list': sidebar_elems}})
    return HttpResponse(template.render(context))

def create(request):
    """
    Create single question
    """
    pass

def favorite(request, question_id):
    """
    Save question for later
    """
    pass

def delete(request, question_id):
    """
    Delete single question
    """
    pass

def rate(request, question_id, score):
    """
    Rate single question
    """
    pass

def view_question(request, question_id):
    """
    View single question
    """
    question = Question.objects.get(id=question_id)
    return render(request, "interview/question.html", {'question': question})

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

