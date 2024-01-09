import asyncio
import time

import httpx

from collect import collecting_result_data

CATEGORY_IDS = [2046, 1502, 2043]
# 2046 - продажа квартир
# 1502 - продажа авто
# 2043 - аренда квартир

start_time = time.time()


async def main():
    async with httpx.AsyncClient() as client:
        tasks = []

        for category_id in CATEGORY_IDS:
            tasks.append(
                asyncio.ensure_future(collecting_result_data(client=client, category_id=category_id)))

        results = await asyncio.gather(*tasks)

        result = []
        for res in results:
            result.extend(res)



asyncio.run(main())
