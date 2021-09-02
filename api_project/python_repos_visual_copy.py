import requests
from requests.api import head

import plotly
from plotly import offline

def get_response():
    # Wykonanie wywołania API i zachowanei otrzymanej odpowiedzi
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Kod stanu: {r.status_code}")
    return r

def get_repo_dicts(r):
    # Przetworzenie wyników
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_project_data(repo_dicts):
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    return repo_links, stars, labels

def make_visualization(repo_links, stars, labels):
    # Utworzenie wizualizacji
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60,100,150)',
            'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Oznaczone największą liczbą gwiazdek projekty Pythona w serwisie Github',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repozytorium',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
            },
        'yaxis': {
            'title': 'Gwiazdki',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
            },
    }
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python.repos.html')

if __name__ == '__main__':
    r = get_response()
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_visualization(repo_links, stars, labels)