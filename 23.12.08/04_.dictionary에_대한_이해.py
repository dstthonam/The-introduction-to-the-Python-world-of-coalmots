# 딕셔너리(dictionary, 사전)

pl = {"C":5, "JAVA":8, "JS":7, "PTYHON":20}

# 갯수 세기 가능 - len(pl)

# 딕셔너리 키값 변경
pl["C"] = 6

# 딕셔너리 키 추가 및 제거
pl["RUBY"] = 3
pl.pop("RUBY")

print(pl)

print(pl["C"])

