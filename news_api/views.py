from os import access
from tabnanny import check
from django.shortcuts import render
import requests
API_KEY_NEWS = 'd0b69496c18e463f888a273cb521ea9f'
API_KEY_WEATHER='aaba2d7cd73f453ca14144033222906'
CAT = 'Technology'
def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    url_for_location='http://ipinfo.io/14.139.162.2 ? token=0680a74dacbc7b'
    response_of_location = requests.get(url_for_location)
    data_of_location = response_of_location.json()
    CITY = data_of_location['city']
    CAN = data_of_location['country']
    url_for_weather=f'http://api.weatherapi.com/v1/current.json?key={API_KEY_WEATHER} &q={CITY}&aqi=no'
    response_of_weather = requests.get(url_for_weather)
    data_of_weather = response_of_weather.json()
    if category:
        url_for_news = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY_NEWS}&country={CAN}'
        response_of_news = requests.get(url_for_news)    
        data_of_news = response_of_news.json()
        articles = data_of_news['articles']
    else:
        url_for_news = f'https://newsapi.org/v2/top-headlines?category={CAT}&apiKey={API_KEY_NEWS}&country={CAN}'
        response_of_news = requests.get(url_for_news)
        data_of_news = response_of_news.json()
        articles = data_of_news['articles']

    weather = {
        'Name' :data_of_weather['location']['name'],
        'temp' :data_of_weather['current']['temp_c'],
        'description' : data_of_weather['current']['condition']['text'],
        'icon' :data_of_weather['current']['condition']['icon'],
    }
    context={
        'weather' : weather,
        'articles' :articles
    }

    return render(request, 'news_api/home.html', context)


