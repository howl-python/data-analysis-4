import csv  # CSV 파일을 줄 칸으로 끊어 읽어주는 파이썬 기본 모듈
import os  # 파일 경로를 다루는 파이썬 기본 모듈

age = 36
message = "제나이는" + str(age) + "살입니다"
# age 라는 과자상자안에  숫자 36을 넣었고 숫자는
# 같이출력할수 없기에 str(문자열)형식으로 변환후
# 나이는 과 살입니다를 같이 출력할수 있게해준다
print(message)

p = float("3.14")
# 실수 float 이고 프린트를 그대로하면 출력이되고
# 타입을 쓰면 어떤형태(실수 정수인지 파악할수있음)
print(p)
print(type(p))

height = 175.5
print(type(height))
age = "20"
age2 = "30"
print(int(age) + int(age2))
# 문자열 숫자를 인트(숫자열) 로 변환후 값을 더한다
# age = 36
# print(" 저는" + str(36) + "살이에요")

# 연산자
print(10 // 5)
# 2 2개씩(몫) 5명이 나눠가짐 10개
print(10 / 5)  # 2개씩나누는것 대신 실수(소수점) 변환함
print(10 % 5)  # 10개를 5명이 나눠가지므로 남은것이없어 0
print(10 % 3)  # 1 9개씩 나눠가지면서 1개가 남음

score = 60
print(score >= 30 and score <= 20)
# 둘중 하나라도 거짓이면 False 둘다 '참' 일떄만 True
print(score >= 30 or score <= 80)
# or 둘중 하나라도 참이면 True 출력
# print(score >= 30 not score <= 80)
# ㄴ 파이썬으로는 맞지않아 and not 이들어가 둘중하나라도 아니면

# 연산자
print((2 + 3) * 5)  # 첫괄호 계산 이후 밖에 있는걸 계산한다
# 할당 연산자
cash = 3500  # 3500 숫자를 캐쉬에 저장
cash += 500  # 500이라는 숫자를 더한후 다시 담기
print(cash)  # 출력후 보여줌

holy = 17 // 5  # 예상   3묶음씩 나눠갖고 남는게 잇음
molly = 17 % 5  # 예상    2개가남음
coach = 15 % 2  # 예상 1 홀수

print(holy)
print(molly)
print(coach)
coin = 100
coin += 50
coin *= 2
print(coin)

word = "python"
print(word[::-1])
