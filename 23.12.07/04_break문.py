# break문의 이해
'''
for a in range(1, 10, 1):
  print(a, "번째 반복했습니다.")
  
  if a == 5:
    break
  
print("반복문을 빠져나왔습니다.")
print("현재 count의 값:", a)
'''
count = 1
while count <= 10:
  print(count, "번째 반복했습니다.")

  if count == 5:
    break
  
  count += 1
print()
print("반복문을 빠져나왔습니다.")
print("현재 count의 값:", count)

