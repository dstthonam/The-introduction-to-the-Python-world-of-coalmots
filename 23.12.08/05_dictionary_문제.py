# 딕셔너리 문제

pl = {"C":5, "JAVA":8, "JS":7, "PYTHON":20}

학생수 = 0
최댓값 = 0

for x in pl:
  print(x, ":", pl[x], "명")
  학생수 += pl[x]
  
  if 최댓값 < pl[x]:
    최댓값 = pl[x]
    언어 = x
    
print()
print("전체 학생수:", 학생수)
print("가장 선호도가 높은 프로그래밍 언어:", 언어)
print("선호 인원:", 최댓값)
print("선호율:", 최댓값/학생수 * 100, "%")

