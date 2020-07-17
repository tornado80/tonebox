import requests
from time import sleep
uri = "https://icons.iconarchive.com/icons/iconicon/alpha-magnets/128/Letter-{}-icon.png"
for i in range(97, 123):
    c = chr(i)
    with open(f"{c}.png","wb") as f:
        f.write(requests.get(uri.format(c)).content)
    #sleep(0.5)
