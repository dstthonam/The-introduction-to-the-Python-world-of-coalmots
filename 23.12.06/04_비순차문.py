# 조건문(선택문) - 순차문, 비순차문

'''
if 조건식: 
  실행할 문장

if 조건식:
  실행할 문장1
  ...
  실행할 문장n
다음문장
'''
print("=" * 10)
기말고사 = int(input("기말고사 성적을 입력하세요: "))
결석 = int(input("결석 횟수를 입력하세요: "))

if 결석 < 3: 
  기말고사 = 기말고사 + 5
  # 기말고사 += 5
print("당신의 최종 점수는", 기말고사, "점 입니다.")
print(">" * 3)
print("=" * 10)
기말고사 = int(input("기말고사 성적을 입력하세요: "))
결석 = int(input("결석 횟수를 입력하세요: "))

if 결석 < 3: 
  기말고사 = 기말고사 + 5
  # 기말고사 += 5
print("당신의 최종 점수는", 기말고사, "점 입니다.")
print(">" * 3)




