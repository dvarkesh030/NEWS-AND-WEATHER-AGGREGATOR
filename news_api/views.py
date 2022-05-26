from django.shortcuts import render
import requests
API_KEY = 'd0b69496c18e463f888a273cb521ea9f'
CAT = 'Technology'
CAN = 'in'

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}&country={CAN}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={CAT}&apiKey={API_KEY}&country={CAN}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)


