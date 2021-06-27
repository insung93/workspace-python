from bs4 import BeautifulSoup
import requests
file = open("scholar.csv", "w",encoding='UTF-8')


keyword = input("키워드 입력 : ")
page = int(input("가져올 페이지 수 입력 : "))

for i in range(1,page+1):
    print("[{} 페이지]********************************".format(i))
    start = (page-1)*10
    link = "https://scholar.google.co.kr/scholar?hl=ko&as_sdt=0,5&q={}&start={}".format(keyword,start);
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
    res = requests.get(link, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    body = soup.find("div", attrs={"id" : "gs_res_ccl_mid"})
    items_title = body.find_all("div", attrs={"class":"gs_ri"})
    for item in items_title:
        title_id = item.find("a", id=True)["id"]
        title = item.find("a",attrs={"id":title_id}).text
        print("[title] : "+title)
        contents = item.find("div",attrs={"class":"gs_rs"}).text
        print(contents)

        file.write("{}, {} \n".format(title,contents))
    
