import time
from datetime import datetime

from parse import get_json_for_rental_estate_items_by_category, get_json_for_item_details
import json


async def collecting_result_data(client, category_id):

    start = time.time()
    response_data = await get_json_for_rental_estate_items_by_category(client, category_id=category_id)
    end = time.time()
    print(f'finished request for category_id={category_id} in {end - start} seconds...')
    
    items = response_data['items']
    result = []

    if category_id == 2046:
        category_name = 'продажа квартир'
    elif category_id == 1502:
        category_name = 'продажа авто'
    elif category_id == 2043:
        category_name = 'аренда квартир'

    for item in items:

        images = []
        for image in item['images']:
            images.append(image['original_url'])

        detail_start = time.time()
        detail = await get_json_for_item_details(client, item_id=item['id'])
        detail_end = time.time()

        for param in detail['params']:
            if param['id'] == 70:
                square = param['value']
            if param['id'] == 952:
                add_from = param['value']

        result.append({
            'title': item['title'],
            'description': item['description'],
            'price': item['price'],
            'city': item['city'],
            'category_name': category_name,
            'images_url': images,
            'phone_number': item['mobile'],
            'user': item['user']['username'],
        })

        with open('output.json', 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=4)

    return result
