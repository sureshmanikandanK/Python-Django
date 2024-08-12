from django.shortcuts import render # type: ignore
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore
# Create your views here.

week_schedule = {
    'sun':'Learn Python',
    'mon':'Learn .Net',
    'tues':'Learn Java',
    'wed':'Learn React',
    'thur':'Learn Angular',
    'fri':'Learn Salesforce',
    'sat':'Learn Aws',
}

def week(request,day):
    days = list(week_schedule.keys())

    if(day>len(week_schedule)):
        return HttpResponseNotFound('Enter 1-7')
    redirect_day = days[day-1]
    redirect_day = reverse('Days',args=[redirect_day])
    return HttpResponseRedirect(redirect_day)
def week_display(request,day):
    try:
        DAYS=week_schedule[day]
        return HttpResponse(DAYS)
    except:
        return HttpResponse('Not Found')
