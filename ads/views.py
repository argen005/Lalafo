import json
import time
from .models import Ad
import subprocess
from django.http import HttpResponse


def parse(request):
    subprocess.run(['python3', 'ads/main.py'])

    json_file_path = 'output.json'
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        ad_data = json.load(json_file)

    for ad_info in ad_data:
        ad_instance = Ad(
            title=ad_info['title'],
            description=ad_info['description'],
            price=ad_info['price'],
            city=ad_info['city'],
            category_name=ad_info['category_name'],
            images_url=json.dumps(ad_info['images_url']),  # Convert list to JSON string
            phone_number=ad_info['phone_number'],
            user=ad_info['user'],
        )
        ad_instance.save()

    return HttpResponse("идет запись в бд")