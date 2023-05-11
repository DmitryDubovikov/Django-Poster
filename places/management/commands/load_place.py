from django.core.management.base import BaseCommand, CommandError

import json
import requests
from places.models import Place, Image


class Command(BaseCommand):
    help = "Load JSON data from the internet"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="url for json file")

    def handle(self, *args, **options):
        url = options["url"]
        with requests.get(url) as response:
            data = json.loads(response.json())
        for item in data:
            obj = Place(**item)
            obj.save()
        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
