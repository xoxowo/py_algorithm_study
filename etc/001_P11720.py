n = input()
numbers = list(input())
sum = 0 

for i in numbers :
    sum += int(i)

print(sum)

"""
실행 결과값
5 -> n = input() 다음행의 리스트에 숫자가 몇 개 들어갈건지 입력 숫자
23456 -> numbers = list(input()) 두번째줄에 숫자 입력하면 list로 아래 for문돌아서 아래 결과값 출력
20 -> print(sum)
"""