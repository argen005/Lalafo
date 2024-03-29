import httpx


async def get_json_for_rental_estate_items_by_category(client, category_id):
    url = f'https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=16&category_id={category_id}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "device": "pc",
    }
    params = {
        'sort_by': 'newest'
    }
    try:
        response = await client.get(url, headers=headers, params=params)
        response_data = response.json()
        
        return response_data
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")


async def get_json_for_item_details(client, item_id):
    url = f'https://lalafo.kg/api/search/v3/feed/details/{item_id}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "device": "pc",
    }
    try:
        response = await client.get(url, headers=headers)
        return response.json()
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
