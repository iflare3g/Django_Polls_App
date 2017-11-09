from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-publish_date')[:5] #last_five_ones
    context = { 
        'latest_questions':latest_questions
    }
    return render(request,'polls/index.html',context)

    
def detail(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    context = {
        'question':question
    }
    return render(request,'polls/detail.html',context)

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {
        'question':question
    }
    return render(request,'polls/results.html',context)
    
def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        context = {
            'question':question,
            'error_message':'Please select a choice.'
        }
        return render(request,'polls/detail.html',context)
    else:
        selected_choice.num_of_votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
    