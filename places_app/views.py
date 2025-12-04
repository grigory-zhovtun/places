from django.shortcuts import render
from .models import Place


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
                "detailsUrl": "TODO",
            }
        }
        places_geojson["features"].append(feature)

    context = {
        "places_geojson": places_geojson
    }
    return render(request, 'index.html', context)
