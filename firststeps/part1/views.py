from django.http  import Http404,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.db.models import F
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.views import generic

class IndexView(generic.ListView):
    template_name = "part1/index.html"
    context_object_name ="latest_question_list"
    def get_queryset(self):
        return  Question.objects.order_by("-pub_date")[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = "part1/detail.html"
# def detail(request,question_id):
    #404 error
    # try:
        # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")
    #get_object_or_404()
    # question = get_object_or_404(Question,pk=question_id)
    # return render(request,"part1/detail.html",{"question":question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = "part1/results.html"
# def results(request,question_id):
    # question = get_object_or_404(Question,pk=question_id)
    # return render(request,"part1/results.html",{"question":question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(
            request,
            "part1/detail.html",
            {
                "question":question,
                "error_message":"You didn't select a choice.",
            }
        )
    else:
        selected_choice.votes =F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("part1:results", args=(question.id,)))