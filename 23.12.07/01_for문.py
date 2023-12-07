# 횟수 제어 반복 for 문을 이용한 예제
'''
print(">" * 3)
print("=" * 6 + "RESTART" + "=" * 6)
for x in range(1,11,1):
  print(x)
print(">" * 3)

주머니 = 0
for x in range(1,11,1):
  주머니 += x
print("1부터 10까지의 합은:", 주머니)
print(">" * 3)
'''

# p.55 예제 3번 

짝수합 = 0
홀수합 = 0

for x in range(1,101,1):
  if 0 == x % 2:
    짝수합 += x
  else:
    홀수합 += x

print("짝수합 =", 짝수합)
print("홀수합 =", 홀수합)

