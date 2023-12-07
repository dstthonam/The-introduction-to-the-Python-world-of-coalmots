# 주사위 굴려서 주사위 눈의 합을 가져감, 4가 나오면 더이상 가져가지 못함

import random

횟수 = 0
점수 = 0

while True:
  횟수 += 1
  주사위 = random.randrange(1,7,1)
  print(횟수, "번째 주사위 눈: ", 주사위)
  
  if 주사위 == 4:
    break
  else: 
    점수 += 주사위

print()
print("주사위 던진 횟수:", 횟수)
print("획득한 점수:" , 점수)

