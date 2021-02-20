import sys
from io import BytesIO

import requests
from PIL import Image

from get_scale import get_scale


def get_map(toponym_to_find, spn="", longt=0, latt=0):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        print('Ошибка в выполнении запроса к серверу')
    else:
        if spn:
            map_params = get_scale(response, spn, longt, latt)
        else:
            map_params = get_scale(response, longt, latt)
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        try:
            response = requests.get(map_api_server, params=map_params)
            return response.content
        except Exception as e:
            print('Ошибка: ', e)

