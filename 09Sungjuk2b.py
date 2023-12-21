# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

names = ['신동엽', '김지현', '이수지']
kors = [30, 40, 50]
engs = [60, 70, 80]
mats = [90, 92, 93]

for i in range(len(names)):
    total = kors[i] + engs[i] + mats[i]
    avg = total / 3
    print(f'이름 : {names[i]:s} , 국어 : {kors[i]}, 영어 : {engs[i]}, 수학 : {mats[i]}')
    print(f'총점 : {total} , 평균 : {avg:.1f}')

#############################################

names = []
kors = []
engs = []
mats = []

for i in range(3):
    print(f'{i + 1}번째 학생 데이터 입력')
    names.append(input('이름은?'))
    kors.append(int(input('국어?')))
    engs.append(int(input('영어?')))
    mats.append(int(input('수학?')))

for i in range(len(names)):
    total = kors[i] + engs[i] + mats[i]
    avg = total / 3
    print(f'이름 : {names[i]:s} , 국어 : {kors[i]}, 영어 : {engs[i]}, 수학 : {mats[i]}')
    print(f'총점 : {total} , 평균 : {avg:.1f}')