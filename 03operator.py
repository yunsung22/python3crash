
# 수식expression
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 => 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

a = 10
b = 20
c = 30

print(a, b, c)

d = 10; e = 20; f = 30;

print(d,e,f)

g, h, i = 10, 20, 30

print(g, h, i)

j = 1_000_000_000

print(j)

PI = 3.14152

print(PI)

print(10/3, 10%3, 10//3)

print(10 ** 1 , 10 ** 2, 10 ** 3)


# 논리식 : 논리연산자(논리 합/곱/부정)를 이용한 수식
# 또한, 둘 이상의 논리식이나 관계식으로 구성된 수식
# 논리식의 경우, 수식의 구성에 따라 단축식 평가short-circuit가 가능


# and 연산시 첫번째 수식의 결과가 F면 단축식평가 적용
print(3 > 5 and 2 < 3)

# or 연산시 첫번째 수식의 결과가 T면 단축식평가 적용
print(2 < 3 or 3 < 5)


# 복합 대입연산자 : 대입연산자와 산술연산자를 결합한 수식
# 보통 수식을 간단히 작성시 사용 - 축약표현
# 변수 = 변수 + 수식 => 변수 += 수식

k = 10
k += 1
print(k)

# 연산자 우선순위
# 괄호내 연산자 -> 단항연산자 -> 산술연산자 -> 관계연산자 -> 논리연산자

# 연산자의 부수적인 기능 - 문자열 연산
# + : 문자열 연결
# * : 문자열 반복 연결

str1 = 'Hello'
str2 = 'World'
print(str1 + str2)

print(123 + int('456'))
print(str(123) + '456')

# 숫자형과 문자형의 논리 연산
# 0 또는 빈 문자열은 False로 인식
# bool 함수를 이용하면 지정한 값의 논리값을 알수있음
print(0 and 'abc', 1 and 'abc')
print('' or 'abc', '' and 'abc')

#문자열 서식화 하기
print('이름 : 홍길동, 나이 : 25')

name, age = '홍길동', 25
print('이름 :', name, '나이 :', age)

print('이름 : %s, 나이 : %d' %(name, age))

print('이름 : {}, 나이 : {}'.format(name, age))

print(f'이름 : {name}, 나이 : {age}')

#구구단
dan = 7
print(f'{dan} X 1 = {dan * 1}')
print(f'{dan} X 2 = {dan * 2}')
print(f'{dan} X 3 = {dan * 3}')
print(f'{dan} X 4 = {dan * 4}')
print(f'{dan} X 5 = {dan * 5}')
print(f'{dan} X 6 = {dan * 6}')
print(f'{dan} X 7 = {dan * 7}')
print(f'{dan} X 8 = {dan * 8}')
print(f'{dan} X 9 = {dan * 9}')
