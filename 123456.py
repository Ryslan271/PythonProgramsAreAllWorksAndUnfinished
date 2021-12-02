import requests

def get_data(response):
    json_response = response.jnos()
    toponym = json_response['response']["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_county = toponym['metaDataProperty']["GeocoderMetaData"]['Address']['Components'][1]['name']
    toponym_province = toponym['metaDataProperty']["GeocoderMetaData"]['Address']['Components'][2]['name']
    toponym_name = toponym_address.split(', ')[-1]
    toponym_index = toponym['metaDataProperty']["GeocoderMetaData"]['Address']['postal_code']
    toponym_coodrinates = toponym['Point']['pos']
    return toponym_name, toponym_province

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-" \ 
"0493-4b70-98ba-98533de7710b&geocode=Хабаровск&format=json"

resp = requests.get(geocoder_request)
county = get_data(resp)
print(f'{county[0]} относится к {county[1]}')

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-" \ 
"0493-4b70-98ba-98533de7710b&geocode=Уфа&format=json"
resp = requests.get(geocoder_request)
county = get_data(resp)
print(f'{county[0]} относится к {county[1]}')

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-" \ 
"0493-4b70-98ba-98533de7710b&geocode=Нижний Новгород&format=json"
resp = requests.get(geocoder_request)
county = get_data(resp)
print(f'{county[0]} относится к {county[1]}')

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-" \ 
"0493-4b70-98ba-98533de7710b&geocode=Калининград&format=json"
resp = requests.get(geocoder_request)
county = get_data(resp)
print(f'{county[0]} относится к {county[1]}')