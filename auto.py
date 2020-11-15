import requests

def googlesearch(query):
    with requests.session() as c:
        url = 'https://www.google.co.in'
        query = {'q': query}
        urllink =   requests.get(url,params=query)
        print(urllink.url)


googlesearch("India")