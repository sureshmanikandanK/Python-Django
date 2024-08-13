from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

month_schdeule = {
    'jan': 'Learn Python',
    'feb': 'Learn .Net',
    'mar': 'Learn Java',
    'apr': 'Learn React',
}

def index(request):
    month = list(month_schdeule.keys())

    return render(request,'rend_details/index.html',{
            'month':month
    })

def monthly_details_by_number(request, month):
    months = list(month_schdeule.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid Month')
    
    redirect_month = months[month - 1]
    redirect_url = reverse('rend_app', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)

def montly_details(request, month):
    try:
        month_text = month_schdeule[month]
        response_data=  render(request,'rend_details/rend.html',{'text':month_text})
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound('This page not found')
