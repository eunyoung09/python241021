import requests
from bs4 import BeautifulSoup
import openpyxl

# 요청할 URL 설정 (크롤링 가능한 웹페이지로 변경)
url = 'https://example-news-site.com'

# 페이지 요청
response = requests.get(url)
html = response.text

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, 'html.parser')

# 기사 제목 찾기 (적절한 태그와 클래스로 변경 필요)
titles = soup.find_all('h2', class_='news-title')

# Excel 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "News Titles"

# 첫 번째 행에 헤더 작성
ws.append(["Article Title"])

# 제목을 Excel에 작성
for title in titles:
    ws.append([title.get_text()])

# 엑셀 파일 저장
wb.save("results.xlsx")
