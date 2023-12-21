

print('오늘 날씨 너무 추워요')
print('오늘 날씨 너무 추워요')
print('오늘 날씨 너무 추워요')
print('오늘 날씨 너무 추워요')

#for문
# for 변수 in range(시작값, 종료값, 증가/감소)
# 반복할 문장
# 반복횟수는 range 로 유추   종료값 - 시작값 - 1

print(list(range(1,11)))

print(list(range(1,11, 2)))

numbers = [1,2,3,4,5,6,7,8,9,10]

for i in range(1,4):
    print('오늘 날씨 너무 추워요')

for num in numbers:
    print(num, end=',')

total = 0
for i in range(1,101):
    total = total + i

print(total)

n = 100
print( (n * (n + 1) ) / 2)

# 구구단 출력
gugudan = input('출력할 단을 입력해 주세요:')

for i in range(1,10):
    print(f'{gugudan} X {i} = {int(gugudan) * i}')

for i in range(2,9,2):
    print(i, end=',')


# 이터러블에 문자열을 넣으면 아이템에는
# 문자열의 첫 문자부터 끝 문자가 순차적으로 저장됨
# 결과적으로 실행문은 문자 개수만큼 반복 실행됨



# while 문