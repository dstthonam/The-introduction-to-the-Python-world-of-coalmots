# 다중 if문: 문제

print("=" * 5)
기말고사 = int(input("기말고사 성적을 입력하세요: "))
결석 = int(input("결석 횟수를 입력하세요: "))

if 결석 < 3: 
  #기말고사 = 기말고사 + 5
  기말고사 += 5
elif 결석 < 5: 
  #기말고사 = 기말고사 + 1
  기말고사 += 1
else:
  #기말고사 = 기말고사 - 5
  기말고사 -= 5
  
print("당신의 최종 점수는", 기말고사, "점 입니다.")


