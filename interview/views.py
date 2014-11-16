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
from interview.forms import QuestionForm


def index(request):
    template = loader.get_template('interview/index.html')
    questions = Question.objects.all()
    categories = {question.category for question in questions}
    sidebar_elems = [{"link": "#", "text": category} for category in categories]
    context = RequestContext(request, {'questions':questions, 'sidebar': {'title': "Categories", 'list': sidebar_elems}})
    return HttpResponse(template.render(context))

def create(request):
    """
    Create single question
    """
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return index(request)
        else:
            print(str(question_form.errors))
    else:
        question_form = QuestionForm()
    return render(request, "interview/create.html", {'question_form': question_form})

def favorite(request, question_id):
    """
    Save question for later
    1. get the user for request
    up=UserProfile.objects.get(user=request.user)
    2. get the question using question_id
    q=Question.objects.get(id=question_id)

    (add favorite field in the personal question)

    3. get the PQ  question 
    pq=personalQuestions.objects.get_or_create(user=up, question=q)
    pq.favorite=not pq.favorite
    pq.save()
    return json success

    http://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python


    """
    up = UserProfile.objects.get(user=request.user)
    q = Question.objects.get(id=question_id)
    pq_fav = personalQuestions.objects.get_or_create(user=up, question=q)
    pq_fav.favorite = not pq.favorite
    pq_fav.save()
    return HttpResponse(json.dumps(pq_fav), content_type="application/json")


def delete(request, question_id):
    """
    Delete single question
    """
    pass

def rate(request, question_id, stars_no):
    """
    Rate single question
        1. get the user for request
    up=UserProfile.objects.get(user=request.user)
    2. get the question using question_id
    q=Question.objects.get(id=question_id)

    (add favorite field in the personal question)

    3. get the PQ  question 
    pq=personalQuestions.objects.get_or_create(user=up, question=q)
    pq.stars=stars_no
    pq.save()
    return json success
    """
    up = UserProfile.objects.get(user=request.user)
    q = Question.objects.get(id=question_id)
    pq_rate = personalQuestions.objects.get_or_create(user=up, question=q)
    pq_rate.stars = stars_no
    pq_rate.save()
    return HttpResponse(json.dumps(pq_rate), content_type="application/json")

def view_all_favorite(request, question_id):
    """
    View all favorite questions
    """

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

