#DemoForm2.py
#DemoForm2.ui(화면) + DemoForm2.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
#웹서버에 요청
import requests

#미리 디자인한 문서를 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#DemoForm2 클래스 선언(QMainWindow)
class DemoForm2(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯 함수 추가
    def firstClick(self):
        url = "https://www.daangn.com/hot_articles"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        f=open("daangn.txt","a+",encoding="utf-8")
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
        f.close()

        self.label.setText("당근마켓 크롤링 완료")  
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭.")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭했.")

# 진입점 생성
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm2()
    myWindow.show()
    app.exec_()
