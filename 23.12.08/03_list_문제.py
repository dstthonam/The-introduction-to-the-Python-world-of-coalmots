# list 문제(최대값, 최소값 빼기)
score = []

for x in range(0,5,1):
  score.append(int(input("-심사위원 점수를 입력해 주세요:")))
print("입력받은 원본 점수:", score)

# 최대값 / 최소값 구하기
'''
최대값 = score[0]
최소값 = score[0]

for x in score:
  if x > 최대값 :
    최대값 = x
    
  if x < 최소값 :
    최소값 = x
'''
최대값 = max(score)
최소값 = min(score)

print("최대점수:", 최대값)
print("최소점수:", 최소값)

score.remove(최대값)
score.remove(최소값)

print("최대/최소 점수를 제외한 점수:", score)
print("최종 점수:", sum(score)/(len(score)))

