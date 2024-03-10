from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

def owner(request):
    return HttpResponse("Hello, world. 788117e4 is the polls index.")

"""
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

"""

# updated 3 classes using the generic view types
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions. """        
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# vote function
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) # corresponds with radio button's name arg
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
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
        # reverse() avoids having to hardcode a URL in view function --> returns string "/polls/3/results/"
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))