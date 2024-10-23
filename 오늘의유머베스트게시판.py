# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #클리앙의 중고장터 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        #검색 객체 생성
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
# <span class="subject_fixed" data-role="list-title-text" title="opus bt-c3100 멀티 충전지 충전기 팝니다. ​">
# 		opus bt-c3100 멀티 충전지 충전기 팝니다. ​
# 						</span>
        for item in list:
                try:
                        title = item.find('a').text.strip()
                        #print(title)
                        if (re.search('이유', title)):
                                 print(title)
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
