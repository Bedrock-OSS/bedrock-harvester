import requests

def download_file(url: str, out: str):
    '''Download file from url and save it to out path.'''
    print(f'Downloading file from {url}')
    data = requests.get(url).content
    with open(out, 'wb') as f:
        f.write(data)
