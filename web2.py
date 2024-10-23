#web2.py

from bs4 import BeautifulSoup
#웹서버에 요청
import requests

url = "https://www.daangn.com/hot_articles"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all("div", {"class":"card-desc"})


for post in posts:
    titleElem = post.find("h2", attrs ={"class":"card-title"})
    priceElem = post.find("div", attrs ={"class":"card-price"})
    regionElem = post.find("div", attrs ={"class":"card-region-name"})
    title = titleElem.text.replace("\n","").strip()
    price = priceElem.text.replace("\n","").strip()
    address = regionElem.text.replace("\n","").strip()
    

    print(f"{title}, {price}, {address}")
    f.write(f"{title}, {price}, {address}\n")
    # #    9,000원
    #   </div>
    #   <div class="card-region-name">
    #     서울 중랑구 면목동
    #   </div>
f.close()