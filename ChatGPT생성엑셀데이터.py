import random
from openpyxl import Workbook

# 전자제품 목록
제품_목록 = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "이어폰", "블루투스 스피커",
    "TV", "모니터", "게임 콘솔", "디지털 카메라", "프린터", "공기청정기",
    "로봇청소기", "전자레인지", "냉장고", "세탁기", "에어컨", "전기밥솥"
]

# 데이터 생성 함수
def 데이터_생성():
    데이터 = []
    for i in range(1, 101):  # 100개의 데이터 생성
        제품ID = f"P{i:03d}"
        제품명 = random.choice(제품_목록)
        수량 = random.randint(1, 100)
        가격 = random.randint(10000, 2000000)  # 10,000원 ~ 2,000,000원
        데이터.append([제품ID, 제품명, 수량, 가격])
    return 데이터

# Excel 파일 생성 및 데이터 저장
def 엑셀_파일_생성(데이터):
    wb = Workbook()
    ws = wb.active
    ws.title = "전자제품 판매 데이터"

    # 헤더 추가
    ws.append(["제품ID", "제품명", "수량", "가격"])

    # 데이터 추가
    for 행 in 데이터:
        ws.append(행)

    # 파일 저장
    wb.save("products.xlsx")
    print("products.xlsx 파일이 생성되었습니다.")

# 메인 실행
if __name__ == "__main__":
    판매_데이터 = 데이터_생성()
    엑셀_파일_생성(판매_데이터)