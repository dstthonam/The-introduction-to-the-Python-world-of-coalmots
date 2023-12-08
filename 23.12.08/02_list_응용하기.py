# list 응용하기

score = [80, 70, 100, 90, 60]

# 총점 = score[0] + score[1] + score[2] + score[3] +score[4]

총점 = 0

'''
for x in range(0,len(score),1):
  총점 += score[x]
평균 = 총점 / len(score)
'''
# for x in score:
#   총점 += x

총점 = sum(score)
평균 = 총점 / len(score)

print("심사위원 점수:", score)
print("철수의 총점:", 총점)
print("철수의 평균:", 평균)

