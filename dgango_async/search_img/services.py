import asyncio
import os

import httpx
import aiofiles

from .models import Image


async def get_link(query: str, current_page: int):
    headers = {'Authorization': 'YZHFJobkAKBQHpwpfKpsCC63LgqmQrfk7vXi3ptyrdJztv6P7Z6uLGPj'}
    params = {'query': query, 'per_page': 1, 'page': current_page}
    url = 'https://api.pexels.com/v1/search'
    
    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers, params=params)
        if res.status_code == 200:
            response = res.json()
            print('current_page', current_page)
            return response.get('photos')[0].get('src').get('original')


def get_link_test(query: str, current_page: int):
    headers = {'Authorization': 'YZHFJobkAKBQHpwpfKpsCC63LgqmQrfk7vXi3ptyrdJztv6P7Z6uLGPj'}
    params = {'query': query, 'per_page': 1, 'page': current_page}
    url = 'https://api.pexels.com/v1/search'
    
    res = httpx.get(url, params=params, headers=headers)
    if res.status_code == 200:
        response = res.json()
        print('current_page', current_page)
        return response.get('photos')[0].get('src').get('tiny')


async def search_image(query: str, count: int):
    current_page = 1
    images = await asyncio.gather(
        *(get_link(query, count) for count in range(current_page, count + 1)),
        return_exceptions=True)
    print(images)
    return images


# get_link_test('fox', 1)
# asyncio.run(search_image('fox', 3))
async def download_file(user_id: int, url: str, query: str):
    path = f"./media/{user_id}/"
    file_name = path + f"{url.split('/')[-1]}"
    os.makedirs(path, exist_ok=True)
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        async with aiofiles.open(file_name, 'wb+') as f:
            await f.write(res.read())
        await Image.objects.acreate(title=query, url=file_name, user_id=user_id)


async def save_images(user_id: int, query: str, count: int) -> object:
    link_images = await search_image(query, count)
    await asyncio.gather(
        *(download_file(user_id, url, query) for url in link_images),
        return_exceptions=True)
    return link_images

# asyncio.run(save_images(1, 'fox', 3))
