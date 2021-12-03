import requests

def Weather(city): 
    api_address='http://api.openweathermap.org/data/2.5/weather?q='
    api_key = '&appid=f34fba4479ffc3e251ddb40f2e8ca3a5'
    url = api_address + city + api_key
    json_data = requests.get(url).json() 
    format_add = json_data['main'] 
    print(format_add) 
    return format_add