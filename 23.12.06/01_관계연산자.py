# 관계 연산자 연습하기23.12.06/01_.py

'''
a = 100
b = 200

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)


전공 = int(input("전공 점수를 입력하세요: "))
결과 = (90 <= 전공)
print("결과:", 결과)
'''

#a = "apple"
#b = "banana"
#b = "cat"
#b = "Apple"

a = "박인성"
b = "이동헌"

'''
문자열 비교
특히 알파벳 비교일 경우: 소문자 > 대문자, a -> z 갈수록 1씩 커짐
한글인 경우: 자음 ㄱ -> ㅎ으로 갈수록 커짐, 모음: ㅏ -> ㅣ 갈수록 커짐, 받침: -> ㅎ으로 갈수록 커짐
'''

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
