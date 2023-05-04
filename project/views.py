import copy
from django.http import HttpResponse
from django.template import loader
from places.models import Place


def index(request):
    template = loader.get_template("index.html")

    features = []
    i = 0
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
        i += 1
        new_feature = copy.deepcopy(feature_template)
        new_feature["geometry"]["coordinates"][0] = place.lng
        new_feature["geometry"]["coordinates"][1] = place.lat
        new_feature["properties"]["title"] = place.title
        new_feature["properties"]["placeId"] = "placeId" + str(i)
        features.append(new_feature)

    places_data = {"type": "FeatureCollection", "features": features}
    context = {"places_data": places_data}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
