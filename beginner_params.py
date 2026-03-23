import requests #imma use queue for this and learn it tomorrow as thats way to much threads
import threading
import time

url = "https://google.com"
url2 = "https://google.com?search="
header = {"User-Agent": "Mozilla/5.0"}
with open("somefile.txt", 'r') as fr:
    fuzz =fr.read().splitlines()
baseline = requests.get(url2, headers=header).text.strip()
vuln = threading.Event()
def param_fuzz(load):
    try:

        payload = {"page": load} # change to param used in query
        time.sleep(0.1) # change if threads arent as bad on server
        response = requests.get(url, params=payload, headers=header)
        if response.text.strip() == baseline: # i know this is bad but im assuimg it doesnt send a search result otherwise id of tired thatbut nah not necessary just looking ofr it dumping as id need a page source to know how it displayed on teh page something ill work on later
            pass
        elif response.status_code not in [404]:
            if response.status_code >= 500 and not vuln.is_set():
                print(f"payload caused a error target is likely vulnerable with this payload: " + str(load))
                vuln.set()
            elif response.status_code == 200:
                print(load)

    except requests.exceptions.ConnectionError:
        pass

threads = []
for fuzzie in fuzz:
    t = threading.Thread(target=param_fuzz, args=(fuzzie,))
    threads.append(t)

for t in threads:
    t.start()
  
for t in threads:
    t.join()

for t in threads:
    t.join()
