import sqlite3
import random

class 식음료DB:
    def __init__(self, db_이름="식음료.db"):
        self.연결 = sqlite3.connect(db_이름)
        self.커서 = self.연결.cursor()
        self.테이블_생성()

    def 테이블_생성(self):
        """식음료 테이블 생성"""
        self.커서.execute('''
            CREATE TABLE IF NOT EXISTS 제품 (
                제품ID INTEGER PRIMARY KEY,
                제품명 TEXT NOT NULL,
                가격 REAL NOT NULL
            )
        ''')
        self.연결.commit()

    def 제품_추가(self, 제품ID, 제품명, 가격):
        """새로운 제품 추가"""
        self.커서.execute('''
            INSERT INTO 제품 (제품ID, 제품명, 가격)
            VALUES (?, ?, ?)
        ''', (제품ID, 제품명, 가격))
        self.연결.commit()

    def 제품_수정(self, 제품ID, 새_제품명=None, 새_가격=None):
        """제품 정보 수정"""
        if 새_제품명 and 새_가격 is not None:
            self.커서.execute('''
                UPDATE 제품
                SET 제품명 = ?, 가격 = ?
                WHERE 제품ID = ?
            ''', (새_제품명, 새_가격, 제품ID))
        elif 새_제품명:
            self.커서.execute('''
                UPDATE 제품
                SET 제품명 = ?
                WHERE 제품ID = ?
            ''', (새_제품명, 제품ID))
        elif 새_가격 is not None:
            self.커서.execute('''
                UPDATE 제품
                SET 가격 = ?
                WHERE 제품ID = ?
            ''', (새_가격, 제품ID))
        self.연결.commit()

    def 제품_삭제(self, 제품ID):
        """제품 삭제"""
        self.커서.execute('''
            DELETE FROM 제품
            WHERE 제품ID = ?
        ''', (제품ID,))
        self.연결.commit()

    def 제품_조회(self):
        """모든 제품 조회"""
        self.커서.execute('SELECT * FROM 제품')
        행들 = self.커서.fetchall()
        for 행 in 행들:
            print(행)

    def 연결_종료(self):
        """DB 연결 종료"""
        self.연결.close()

# 샘플 데이터 생성
def 샘플_데이터_생성():
    음료 = ["커피", "주스", "차", "탄산음료", "물"]
    음식 = ["샌드위치", "샐러드", "파스타", "피자", "햄버거"]
    제품_종류 = 음료 + 음식
    db = 식음료DB()

    # 100개의 샘플 데이터 추가
    for i in range(1, 101):
        제품ID = i
        제품명 = random.choice(제품_종류) + f" {i:03d}"
        가격 = round(random.uniform(1000, 20000), -2)  # 100원 단위로 반올림
        db.제품_추가(제품ID, 제품명, 가격)

    # 데이터 조회 및 출력
    print("생성된 샘플 데이터:")
    db.제품_조회()

    # DB 연결 종료
    db.연결_종료()

# 실행
샘플_데이터_생성()