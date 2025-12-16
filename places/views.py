from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_detail', args=[place.id]),
            }
        } for place in Place.objects.all()
    ]

    places_geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    context = {
        'places_geojson': places_geojson
    }
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    image_urls = [img.image.url for img in place.imgs.all()]

    place_data = {
        'title': place.title,
        'imgs': image_urls,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        }
    }

    return JsonResponse(
        place_data,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )