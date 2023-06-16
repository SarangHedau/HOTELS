from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def home(request):
    amenities = Amenities.objects.all()
    context = {'amenities': amenities}
    return render(request, 'home.html',context)

def api_hotels(request):
    hotels_objs = Hotels.objects.all()

    hotel_price = request.GET.get('hotel_price')
    if hotel_price:
        hotels_objs = hotels_objs.filter(hotel_price__lte = hotel_price)

    amenities = request.GET.get('amenities')
    if amenities:
        amenities = amenities.split(',')
        am = []
        for a in amenities:
            try:
                am.append(int(a))
            except Exception as e:
                pass
        hotels_objs = hotels_objs.filter(amenities__in = am).distinct()

    payload = []
    for hotel_obj in hotels_objs:
        result = {}
        result['hotel_name'] = hotel_obj.hotel_name
        result['hotel_description'] = hotel_obj.hotel_description
        result['hotel_image'] = hotel_obj.hotel_image
        result['hotel_price'] = hotel_obj.hotel_price
        payload.append(result)
    return JsonResponse(payload, safe=False)