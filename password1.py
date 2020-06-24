import requests

url='https://api.pwnedpasswords.com/range/'+'E1FA7'

res=requests.get(url)
print(res)