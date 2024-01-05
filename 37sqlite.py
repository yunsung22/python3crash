# insert
# 멤버 테이블에 저장
import sqlite3

#회원정보 입력
userid = input('아이디')
passwd = input('패스워드')
name = input('이름')
email = input('이메일')

conn = sqlite3.connect('db/bigdata.db')
cursor = conn.cursor()

# sql
# sql = f"INSERT INTO MEMBER VALUES ('{userid}', '{passwd}', '{name}', '{email}')"
sql = "INSERT INTO MEMBER VALUES (?, ?, ?, ?)"
params = (userid, passwd, name, email)

try:
    cursor.execute(sql, params)
    conn.commit()
    print(f"데이터베이스에 레코드 {cursor.rowcount}행이 성공적으로 추가되었습니다.")
except sqlite3.Error as e:
    print("데이터베이스 오류:", e)
finally:
    cursor.close()
    conn.close()



# 사용자로부터 입력 받은 데이터
params = {
    'userid': input('수정할 아이디: '),
    'passwd': input('수정할 패스워드: '),
    'name': input('수정할 이름: '),
    'email': input('수정할 이메일: ')
}

conn = sqlite3.connect('db/bigdata.db')
cursor = conn.cursor()

# sql
sql = ("UPDATE member "
       "SET passwd = :passwd, name = :name, email = :email "
       "WHERE userid = :userid")

try:
    cursor.execute(sql, params)
    conn.commit()
    print(f"데이터베이스에 레코드 {cursor.rowcount}행이 성공적으로 수정 되었습니다.")
except sqlite3.Error as e:
    print("데이터베이스 오류:", e)
finally:
    cursor.close()
    conn.close()


# 사용자로부터 입력 받은 데이터
params = {
    'userid': input('삭제할 아이디: ')
}

conn = sqlite3.connect('db/bigdata.db')
cursor = conn.cursor()

# sql
sql = "DELETE FROM member WHERE userid = :userid"

try:
    cursor.execute(sql, params)
    conn.commit()
    print(f"데이터베이스에 레코드 {cursor.rowcount}행이 성공적으로 삭제 되었습니다.")
except sqlite3.Error as e:
    print("데이터베이스 오류:", e)
finally:
    cursor.close()
    conn.close()