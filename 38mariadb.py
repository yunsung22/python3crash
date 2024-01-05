# mariadb 로 데이터 다루기
# 모듈 설치

import pymysql

url = 'url'
user = 'user'
password = 'password'
database = 'database'

# MySQL에 접속
connection = pymysql.connect(
    host=url,
    user=user,
    password=password,
    database=database,
    charset='utf8mb4',  # 문자 인코딩 설정
)

try:
    with connection.cursor() as cursor:
        # SQL 쿼리 실행
        sql_query = "SELECT * FROM member"
        cursor.execute(sql_query)

        # 결과 가져오기
        result = cursor.fetchall()
        for row in result:
            print(row)

except pymysql.Error as e:
    print(f"MySQL 연결 오류: {e}")

finally:
    # MySQL 연결 닫기
    connection.close()