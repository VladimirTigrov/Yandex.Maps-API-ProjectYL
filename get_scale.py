def get_scale(response):
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    lower_corner_longitude, lower_corner_lattitude = toponym["boundedBy"]["Envelope"]["lowerCorner"].split(" "
                                                                                                           )
    upper_corner_longitude, upper_corner_lattitude = toponym["boundedBy"]["Envelope"]["upperCorner"].split(" "
                                                                                                           )

    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    delta = "0.005"
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "bbox": f'{lower_corner_longitude},{lower_corner_lattitude}~{upper_corner_longitude},{upper_corner_lattitude}',
        "l": "map",
        "pt": f'{",".join([toponym_longitude, toponym_lattitude])},pm2ywl'
    }
    return map_params
