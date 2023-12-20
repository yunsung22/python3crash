# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리


# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복 허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근(참조)하려면 변수[인덱스] 형식을 사용

#과일 데이터 저장
fruits = ['사과', '포도', '수박', '참외', '배', '자두']

print(fruits)

# 저녁 메뉴를 리스트로 선언
menus = ['라면', '돈까스', '냉면', '자장면']

print(menus[0])

#리스트 동적으로 생성
menus = []

menus.append("라면")
menus.append("돈까스")
menus.append("자장면")

print(menus)

menus.insert(2, "냉면")

print(menus)

menus[3] = '탕수육'

print(menus)

# 값으로 삭제
menus.remove('탕수육')
menus.pop(2)
menus.pop()

print(menus)

sjs = []

sj = ['수지', 30, 60, 90]
sjs.append(sj)

sj = ['지현', 30, 60, 90]
sjs.append(sj)

print(sjs)