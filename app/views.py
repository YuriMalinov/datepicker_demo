from datetime import date, timedelta
from django.shortcuts import render
from django import forms
from django_bootstrap3_daterangepicker.fields import DateRangeField


class TestForm(forms.Form):
    period = DateRangeField()


# Create your views here.
def index(request):
    period = None
    if request.POST:
        form = TestForm(request.POST)
        if form.is_valid():
            period = form.cleaned_data['period']
    else:
        form = TestForm(initial={"period": (date.today() - timedelta(days=7), date.today())})

    return render(request, 'index.html', {
        'form': form,
        'period': period,
    })
