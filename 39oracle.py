# oracle db 로 데이터 다루기
import cx_Oracle

def connect_to_oracle(username, password, host, port, service_name):
    try:
        # Oracle DB에 연결
        connection = cx_Oracle.connect(user=username, password=password,
                                       dsn=f"{host}:{port}/{service_name}")

        if connection:
            print("Oracle DB에 연결되었습니다.")
            return connection
        else:
            print("Oracle DB 연결 실패")
            return None

    except cx_Oracle.DatabaseError as e:
        print(f"Oracle DB 연결 오류: {e}")
        return None

def execute_select_query(connection, query):
    try:
        # 커서 생성
        cursor = connection.cursor()

        # SELECT 쿼리 실행
        cursor.execute(query)

        # 결과 출력
        for row in cursor.fetchall():
            print(row)

    except cx_Oracle.DatabaseError as e:
        print(f"쿼리 실행 오류: {e}")

    finally:
        # 커서 닫기
        if cursor:
            cursor.close()

def close_connection(connection):
    # 연결 닫기
    if connection:
        connection.close()
        print("Oracle DB 연결이 닫혔습니다.")

# 사용 예시
username = "username"
password = "password"
host = "host"
port = "port"
service_name = "service_name"

# Oracle DB에 연결
oracle_connection = connect_to_oracle(username, password, host, port, service_name)

# SELECT 쿼리 실행 및 결과 출력
if oracle_connection:
    select_query = "select Country, Medal, COUNT(*) from SUMMERMEDALS2 group by Country, Medal"
    execute_select_query(oracle_connection, select_query)

    # 연결 닫기
    close_connection(oracle_connection)

