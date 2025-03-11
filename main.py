import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlsplit
from requests.exceptions import HTTPError
from telegram.error import TelegramError, Unauthorized
from random import randint
from download_web_image import download_image
from post_image_tg import post_image


LAST_COMICS_NUMBER = 3000


def get_filename(url):
    path = Path(urlsplit(url).path)
    return path.name


def fetch_comics_info(comics_num=None):
    if comics_num:
        url = f'https://xkcd.com/{comics_num}/info.0.json'
    else:
        url = 'https://xkcd.com/info.0.json'
    response = requests.get(url=url)
    response.raise_for_status()
    response_body = response.json()
    comment = response_body['alt']
    image_url = response_body['img']
    return comment, image_url


def main():
    load_dotenv()
    try:
        comment, image_url = fetch_comics_info(randint(1, LAST_COMICS_NUMBER))
    except HTTPError as err:
        print(f'Не удалось загрузить картинку. Ошибка: {err}')
        return
   
    image_name = get_filename(image_url)
    image_path = Path(image_name)
    try:
        download_image(url=image_url, filepath=image_path)
    except HTTPError as err:
        print(f'Не удалось загрузить картинку. Ошибка: {err}')
        return
    
    chat_id = os.environ['TG_CHAT_ID']
    token = os.environ['TG_TOKEN']
    try:
        post_image(filepath=image_path,
                   caption=comment,
                   chat_id=chat_id,
                   token=token)
    except Unauthorized:
        print(f'Не удалось опубликовать картинку. Неверный токен.')
        return
    except TelegramError as err:
        print(f'Не удалось опубликовать картинку. Ошибка: {err.message}')
        return
    finally:
        image_path.unlink()


if __name__ == '__main__':
    main()
