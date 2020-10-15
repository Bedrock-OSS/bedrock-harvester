import requests

RP_INPUT = 'https://aka.ms/resourcepacktemplate'
BP_INPUT = 'https://aka.ms/behaviorpacktemplate'

def download_file(url: str, out: str):
    '''Download file from url and save it to out path.'''
    print(f'Downloading file from {url}')
    data = requests.get(url).content
    with open(out, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    download_file(BP_INPUT, 'bp.zip')
    download_file(RP_INPUT, 'rp.zip')
