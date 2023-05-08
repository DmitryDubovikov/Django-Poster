from django.core.management.base import BaseCommand, CommandError

# from django.apps import apps
import json
import requests
from places.models import Place, Image


class Command(BaseCommand):
    help = "Load JSON data from the internet"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="url for json file")

    # def get_json_url(self):
    #     return apps.get_app_config("places").path

    def handle(self, *args, **options):
        url = options["url"]
        with requests.get(url) as response:
            print(response)
            print(json.loads(response.content))

            # data = json.loads(response.read())
            # data = json.loads(response.json())
            data = [1, 2]
        for item in data:
            print(item)
            # obj = Place(**item)
            # obj.save()
        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
