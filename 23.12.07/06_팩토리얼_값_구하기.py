# 정수 입력값을 하나 적고, 입력값의 팩토리얼 값을 출력하는 프로그램

입력값 = int(input("정수 하나를 입력하세요: "))

# for 구문으로 팩토리얼 값 구하기
팩토리얼 = 1
for x in range(입력값,0,-1): # range(1,입력+1,1)
  팩토리얼 *= x
  
print("팩토리얼 값은:", 팩토리얼)

# while 구문으로 팩토리얼 값 구하기
'''
팩토리얼 = 1

while 입력값 > 0:
  팩토리얼 *= 입력값
  입력값 -= 1
  
print("팩토리얼 값은: ", 팩토리얼)
print(">" * 3)
'''