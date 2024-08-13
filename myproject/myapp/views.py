from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# def index(request):
#     return HttpResponse('This works')
# def jan(request):
#     return HttpResponse('This is jan')
# def feb(request):
#     return HttpResponse('This is feb')

month_schdeule = {
    'jan':'Learn Python',
    'feb':'Learn .Net',
    'mar':'Learn Java',
    'apr':'Learn React',
}

def monthly_details_by_number(request,month):
    months = list(month_schdeule.keys())

    if(month>len(months)):
        return HttpResponseNotFound('Invalid Month')
    redirect_month = months[month-1]
    redirect_month = reverse('myapp',args=[redirect_month])
    return HttpResponseRedirect(redirect_month)

def montly_details(request,month):
    try:
        month_text = month_schdeule[month]
        return HttpResponse(month_text)
    except:
        return HttpResponseNotFound('This page not found')
