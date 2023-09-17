import requests


class WeatherStackUtils:

    @classmethod
    def search_weather(cls, name):
        params = {
            'access_key': '664a2227248f1937f7b7b2ecee63cf11',
            'query': name
        }
        api_result = requests.get('http://api.weatherstack.com/current', params)
        api_response = api_result.json()
        return api_response


# 

# 

# print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))