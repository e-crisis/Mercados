from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Transport
import json

# Create your views here.

def ChartView(request):
    transport_data = list(Transport.objects.filter(assured_buy=True).values(
        'id', 'fuel_type', 'car_name', 'yr_mfr', 'date_mfr', 'kms_run', 'sale_price',))
    print("transport data: ", transport_data)
    template = loader.get_template('visualize/chart.html')
    context = {
        'transport_data': transport_data,
    }
    return HttpResponse(template.render(context, request))
