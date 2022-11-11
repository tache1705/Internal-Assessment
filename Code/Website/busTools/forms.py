from django import forms
from django.forms import ModelForm
from .models import BreakEven, Decision, Graphing, ForceField


class BreakEvenForm(ModelForm):
    class Meta:
        model = BreakEven
        fields = "__all__"


class DecisionForm(ModelForm):
    class Meta:
        model = Decision
        fields = "__all__"


class ForceFieldForm(ModelForm):
    class Meta:
        model = ForceField
        fields = "__all__"


class GraphingForm(ModelForm):
    class Meta:
        model = Graphing
        fields = "__all__"