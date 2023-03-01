from os import access
import openai
from tabnanny import check
from django.shortcuts import render
import requests
API_KEY_NEWS = 'pub_1806464d95438a9cf5e9b5d5b7cf1066709cc'
API_KEY_WEATHER='aaba2d7cd73f453ca14144033222906'
CAT = 'Technology'
openai_api_key = "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"

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    topic = request.GET.get('topic')
    url_for_location='http://ipinfo.io/14.139.162.2 ? token=0680a74dacbc7b'
    response_of_location = requests.get(url_for_location)
    data_of_location = response_of_location.json()
    CITY = data_of_location['city']
    CAN = data_of_location['country']
    url_for_weather=f'http://api.weatherapi.com/v1/current.json?key={API_KEY_WEATHER} &q={CITY}&aqi=no'
    response_of_weather = requests.get(url_for_weather)
    data_of_weather = response_of_weather.json()
    if topic:
        url_of_chatgpt = f'https://api.openai.com/v1/engines/text-davinci-003/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_api_key}',
                }

        data = {
            'prompt': topic,
            'max_tokens': 50,
            'temperature': 0.7,
            }
        response = requests.post(url_of_chatgpt, headers=headers, json=data)
        if response.status_code == 200:
            content = response.json()['choices'][0]['text']
        else:
            print(f"Error: {response.status_code} - {response.reason}")

    if category:
        url_for_news = f'https://newsdata.io/api/1/news?apikey=pub_1806464d95438a9cf5e9b5d5b7cf1066709cc&category={category}&country=in'
        response_of_news = requests.get(url_for_news)    
        data_of_news = response_of_news.json()
        articles = data_of_news['results']
    else:
        url_for_news = f'https://newsdata.io/api/1/news?apikey=pub_1806464d95438a9cf5e9b5d5b7cf1066709cc&country=in&category={CAT}'
        response_of_news = requests.get(url_for_news)
        data_of_news = response_of_news.json()
        articles = data_of_news['results']

    weather = {
        'Name' :data_of_weather['location']['name'],
        'temp' :data_of_weather['current']['temp_c'],
        'description' : data_of_weather['current']['condition']['text'],
        'icon' :data_of_weather['current']['condition']['icon'],
    }
    context={
        'weather' : weather,
        'articles' :articles,
        'content' : content
    }

    return render(request, 'news_api/home.html', context)


