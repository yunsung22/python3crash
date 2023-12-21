# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

names = ['신동엽', '김지현', '이수지']
kors = [30, 40, 50]
engs = [60, 70, 80]
mats = [90, 92, 93]

total = kors[0] + engs[0] + mats[0]
avg = total / 3

print(f'이름 : {names[0]:s} , 국어 : {kors[0]}, 영어 : {engs[0]}, 수학 : {mats[0]}')
print(f'총점 : {total} , 평균 : {avg:.1f}')

#############################################

total = kors[1] + engs[1] + mats[1]
avg = total / 3

print(f'이름 : {names[1]:s} , 국어 : {kors[1]}, 영어 : {engs[1]}, 수학 : {mats[1]}')
print(f'총점 : {total} , 평균 : {avg:.1f}')

#############################################

total = kors[2] + engs[2] + mats[2]
avg = total / 3

print(f'이름 : {names[2]:s} , 국어 : {kors[2]}, 영어 : {engs[2]}, 수학 : {mats[2]}')
print(f'총점 : {total} , 평균 : {avg:.1f}')