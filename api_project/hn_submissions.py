from operator import itemgetter

import requests

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

# Przetworzenie informacji o każdym artykule
submission_ids =  r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Przygotowanie oddzielnego wywołania API dla każdego artykułu
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Utworzenie słownika dla każdego artykułu
    if 'descendants' in response_dict:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    else:
        continue

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTytuł: {submission_dict['title']}")
    print(f"Łącze do dyskusji: {submission_dict['hn_link']}")
    print(f"Liczba komentarzy: {submission_dict['comments']}")