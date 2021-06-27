from bs4 import BeautifulSoup
import requests

link = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8";
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
res = requests.get(link, headers=headers)
print(res)
soup = BeautifulSoup(res.text, "html.parser")

item = soup.find("div", attrs={"class" : "main_info"})

today_temp = item.find("span", attrs={"class":"todaytemp"}).text

min_temp=item.find("span", attrs={"class":"min"}).find("span",attrs={"class":"num"}).text
max_temp=item.find("span", attrs={"class":"max"}).find("span",attrs={"class":"num"}).text

lv4=item.find("span", attrs={"class":"lv4"}).find("span",attrs={"class":"num"}).text

item2 = soup.find("div", attrs={"class" : "sub_info"})
lv2=item2.find_all("dd", attrs={"class":"lv2"})[0].find("span", attrs={"class":"num"}).text.replace("㎍/㎥","")


print("현재 온도 : "+today_temp)
print("최고-최저온도: {}/{}".format(min_temp,max_temp))
print("미세먼지 지수: "+lv2)
print("자외선: "+lv4)

# file=open("text.txt","w")
# file.write(todaytemp+"\n")
# file.write(min_temp+"\n")
# file.write(max_temp+"\n")
# file.write(lv4+"\n")

# file.readline()
# file.readline()
# file.readline()
# file.readline()
# file.close()