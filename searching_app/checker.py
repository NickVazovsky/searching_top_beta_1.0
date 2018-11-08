import requests

def check_url(url):
    try:
        status = requests.get(url)
    except Exception as e:

        return False
    else:
        return True