# 선택문 응용 문제 2

print("=" * 10)
이름 = input("당신의 이름을 입력해 주세요:")
전공 = int(input("전공 점수를 입력해주세요:"))
영어 = int(input("영어 점수를 입력해주세요:"))

평균 = (전공 + 영어)/2
print("평균:", 평균)

if 전공 >= 80 and 영어 >= 80:
  print(이름, "님은 합격입니다.")
else:
  print(이름, "님은 불합격입니다.")


