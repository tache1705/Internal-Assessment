from django.shortcuts import render
from .forms import BreakEvenForm, DecisionForm, GraphingForm, ForceFieldForm
from .models import BreakEven, Decision, Graphing, ForceField
from django.http import HttpResponseRedirect


def break_even(request):
    submitted = False
    if request.method == "POST":
        form = BreakEvenForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/begraph")
    else:
        form = BreakEvenForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "break.html", {"form": form, "submitted": submitted})


def begraph(request):
    be_graph = BreakEven.objects.all()
    return render(request, 'begraph.html',
                  {'be_graph': be_graph})


def decision_tree(request):
    submitted = False
    if request.method == "POST":
        form = DecisionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/treediagram")
    else:
        form = DecisionForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "decision.html", {"form": form, "submitted": submitted})


def treediagram(request):
    tree_diagram = Decision.objects.all()
    return render(request, 'treediagram.html',
                  {'tree_diagram': tree_diagram})


def force_field(request):
    submitted = False
    if request.method == "POST":
        form = ForceFieldForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ffdiagram")
    else:
        form = GraphingForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "forceField.html", {"form": form, "submitted": submitted})


def ffdiagram(request):
    ff_diagram = ForceField.objects.all()
    return render(request, 'ffdiagram.html',
                  {'force_field_diagram': ff_diagram})


def graphing(request):
    submitted = False
    if request.method == "POST":
        form = GraphingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/graphdiagram")
    else:
        form = GraphingForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "graphing.html", {"form": form, "submitted": submitted})


def graphdiagram(request):
    graph_diagram = Graphing.objects.all()
    return render(request, 'graphdiagram.html',
                  {'graph_diagram': graph_diagram})
