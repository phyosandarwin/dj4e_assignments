from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from .models import Question

def owner(request):
    return HttpResponse("Hello, world. 788117e4 is the polls index.")

# To call this view file, we need to map it to a URL - and for this we need a URLconf which is created in a file called urls.py
# load a template, fill a context and return an HttpResponse object with the result of the rendered template
# Alt: django.shortcuts's render(), e.g. render(request, "polls/index.html", context)
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html") # wouldnt be necc if u use above shortcut
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


# show question if id exists, otherwise handle 404 error
# you can use get_object_or_404() as shortcut to handle both scenarios
# e.g. get_object_or_404(Question, pk=question_id) --> 1st argument is Django model
def detail(request, question_id):
    try:
        question = Question.objects.get(pk= question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)