import requests
from bs4 import BeautifulSoup

url=requests.get('https://news.ycombinator.com/newest')
#print(url.text)
soup=BeautifulSoup(url.text,'html.parser')
#print(soup.body.contents)
#print(soup.find_all('div'))
#print(soup.find_all('a'))

# print(soup.a)
# print(soup.find('a'))
# print(soup.title)
# print(soup.find(id='score_23562367'))
# print(soup.select('#score_23562367'))
votes=soup.select('.score')
links=soup.select('.storylink')
print(votes[0])
print(links[0])

def hacker_1(links, votes):
    hn=[]
    for i,j in enumerate(links):
        title=links[i].getText()
        hn.append(title)
    return hn

print(hacker_1(links, votes))
