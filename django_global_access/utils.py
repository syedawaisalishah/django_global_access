import requests

def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except:
        return None
