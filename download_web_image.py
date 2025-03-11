import requests


def download_image(url, filepath, query_params=None):
    response = requests.get(url, query_params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)
