#성적처리프로그램 v1

# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함

name = '홍길동'
kor = 30
eng = 60
mat = 90

total = kor + eng + mat
avg = total / 3

print(f'이름 : {name:s} , 국어 : {kor}, 영어 : {eng}, 수학 : {mat}')
print(f'총점 : {total} , 평균 : {avg:.1f}')