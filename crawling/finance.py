from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

link="https://finance.naver.com/"
req = Request(link)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

# subject = soup.find('a').text
# print(subject)

a = soup.find_all('a')
print(a)

b = soup.find('a', attrs={"class" : "child1"})