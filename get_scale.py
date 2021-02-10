def get_scale(response, spn=""):
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
    if not spn:
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": f'{float(upper_corner_longitude) - float(lower_corner_longitude)},{float(upper_corner_lattitude) - float(lower_corner_lattitude)}',
            "l": "map",
            "pt": f'{",".join([toponym_longitude, toponym_lattitude])},pm2ywl'
        }
    else:
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": f'{spn},{spn}',
            "l": "map",
            "pt": f'{",".join([toponym_longitude, toponym_lattitude])},pm2ywl'
        }
    return map_params
