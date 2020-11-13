import requests

N = 300

list_urls = ['https://vk.com/',
             'https://www.youtube.com/',
             'https://www.netflix.com/',
             'http://www.fa.ru/',
             'https://github.com/']

for url in list_urls:
    for i in range(N):
        response = requests.get(url)
        if response.status_code != 200:
            print(f'{url} — #{i} — code: {response.status_code}')
        else:
            print(f'{url} — #{i}')