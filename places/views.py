import copy
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import render
from places.models import Place


def index(request):
    features = []
    feature_template = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [1, 1]},
        "properties": {
            "title": "title",
            "placeId": "placeId",
            "detailsUrl": "detailsUrl",
        },
    }

    places = Place.objects.all()

    for place in places:
        new_feature = copy.deepcopy(feature_template)
        new_feature["geometry"]["coordinates"][0] = place.lng
        new_feature["geometry"]["coordinates"][1] = place.lat
        new_feature["properties"]["title"] = place.title
        new_feature["properties"]["placeId"] = "placeId" + str(place.id)
        new_feature["properties"]["detailsUrl"] = reverse(
            "place-detail", kwargs={"pk": place.id}
        )
        features.append(new_feature)

    places_data = {"type": "FeatureCollection", "features": features}
    context = {"places_data": places_data}
    return render(request, "index.html", context)


def place(request, pk=None):
    obj = get_object_or_404(Place, pk=pk)
    data_dict = {
        "title": obj.title,
        "imgs": [],
        "description_short": obj.description_short,
        "description_long": obj.description_long,
        "coordinates": {"lng": obj.lng, "lat": obj.lat},
    }
    images = obj.images.all()
    for im in images:
        data_dict["imgs"].append(im.image.url)
    return JsonResponse(data_dict)
