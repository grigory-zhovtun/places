from django.shortcuts import render
from .models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.lng,
                    place.lat
                ]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_detail', args=[place.id]),
            }
        }
        places_geojson["features"].append(feature)

    context = {
        "places_geojson": places_geojson
    }
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    image_urls = [img.image.url for img in place.imgs.all()]

    place_data = {
        "title": place.title,
        "imgs": image_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        }
    }

    return JsonResponse(
        place_data,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )