import requests
r = requests.get('https://car-happy.ru/site_search/',{"search_term" : "герметик","search__button" : "1"})
print(r.text)
