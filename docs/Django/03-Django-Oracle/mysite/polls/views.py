from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.urls import reverse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, World. You're at the polls index.")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.htm")
    # output = "\n".join([q.question_text for q in latest_question_list])
    context = {
        "latest_question_list" : latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,"polls/index.htm",context)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk = question_id)
        question_choice_set = question.choice_set.all()
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.htm",{"question":question,"choice_set":question_choice_set})


def results(request, question_id):
    # response = f"You're looking at the results of {question_id}"
    # return HttpResponse(response)
    question = get_object_or_404(Question,pk = question_id)
    return render(request,"polls/results.htm",{"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.htm",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
