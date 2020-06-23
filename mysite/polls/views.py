from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    #List Comprehensions
    # output =", ".join(q.question_text for q in latest_questions)
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #  print(request)
    #  return HttpResponse(f"This is the detail view  of the question: {question_id}")
    question = Question.objects.get(pk = question_id)
    return render(request, "polls/detail.html", {'question': question})
    
def results(request, question_id):
    return HttpResponse(f"These  are the results of the question: {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Vote on question:  {question_id}")




