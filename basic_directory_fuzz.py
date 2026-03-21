import requests

url = "https://www.google.com"
header = {"User-Agent": "Mozilla/5.0"}
with open("/usr/share/wordlists/dirbuster/directoryList.txt", 'r') as f:
    words = f.read().splitlines()
def function(file):
    for i in file:
        try:
            response = requests.get(url + '/' + i, headers=header, timeout=5)
            if response.status_code in (200, 301, 302, 403):
                print(i + " is a path!")
        except requests.exceptions.RequestException as e:
            pass


function(words)
