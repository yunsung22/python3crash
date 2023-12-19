
# 변수
# 어떠한 값을 저장하는 장소를 기억하기 쉽게 문자형태로 나타낸 것
# 변수에 값이 저장되는 공간을 메모리라 함
# 변수에 값을 넣으라고 선언하면,
# 시스템상의 메모리 어딘가에 공간을 확보하고
# 그 공간의 실제주소와 이름을 매핑함

name = '홍길동'
age = 99

Name = '일지매'

#  변수에 저장된 값을 출력
print(name, age, Name)


# 파이썬의 자료형(data-type)
# 정적 타입 : 변수 선언시 자료형도 같이 표시
#            (String name = "홍길동")
#            (name = 123) (오류발생-선언시 자료형과 값의 유형이 다름)

# 동적 타입 : 변수 선언시 자료형은 생략 가능, 추론기능으로 자동할당,
#            또한, 변수에 대입하는 값에 따라 자료형이 바뀜
#            (name = '홍길동')
#            (name = 123) (문제없음-변수의 자료형은 자동으로 변경)

name = 123


# ex) 회원정보 저장용 변수 선언
# 아이디, 비번, 이름, 나이, 이메일,
# 결혼여부, 보유금액, 등록일

userid = 'abc123'
passwd = 'passwd'
name = '홍길동'
age = 18
email = 'yunsung@gmail.com'
isMarried = False
hasMoney = 100000
reg_date = '2023-12-19 16:15:35'

# 정수 자료형
# 소수점 이하의 값이 없는 수
# 123 , 0b0101010 이진수
int1 = 123
int2 = 0b0101010

print(int1, int2, bin(int2))

# 실수 자료형
float1 = 10.0
flaot2 = 123456e-3

print(float1, flaot2)

# 문자 자료형
str1 = 'Hello World'
str2 = 'Hello, \nWorld'
str3 = 'Hello \
World'
str4 = '''Hello, 
World
'''

print(str1, str2, str3, str4)

# Boolean 자료형
# 참 , 거짓을 나타내는 자료형
bool1 = True
bool2 = False
bool3 = 0
bool4 = ''
bool5 = 123
bool6 = '11111'

print(bool1, bool2, bool(bool3), bool(bool4), bool(bool5), bool(bool6))


# 유효숫자e지수 표현법으로 되어 있는 다음 숫자를 보통의 소숫점 표현으로 나타내라.
# 5e8
# 5.6e3
# -2.1e2
# -3.4e-1


# 다음 숫자를 유효숫자e지수 표현법으로 나타내라. 유효숫자는 정수가 되어야 한다.
# 3.141592
# 2.718
# 1.4
# 1.73
