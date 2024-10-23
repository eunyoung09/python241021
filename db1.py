#db1.py
import sqlite3

# 메모리에 임시 데이터베이스 생성
# 영구적으로 파일에 저장
con = sqlite3.connect(r"c:\work\sample.db")
# 커서 인스턴스 생성
cur = con.cursor()

# 테이블 생성
cur.execute("CREATE TABLE if not exists PhoneBook(Name text, Phonenum text);")

# 1건 데이터 삽입
cur.execute("INSERT INTO PhoneBook VALUES('derick', '010-1111-1111');")
# 입력 파라메터 처리
name = "alex"
phoneNumber = "010-2222-2222"
cur.execute("INSERT INTO PhoneBook VALUES(?, ?);", (name, phoneNumber))
#여러건 데이터 삽입
datalist = (("tom", "010-3333-3333"), ("john", "010-4444-4444"))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", datalist)

# 입력 데이터 확인
cur.execute("SELECT * FROM PhoneBook;")
#for row in cur:
#    print(row[0], row[1])
print(cur.fetchall())

# 완료(입력, 수정, 삭제)
con.commit()
con.close()

