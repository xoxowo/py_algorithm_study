n = input()
numbers = list(input())
sum = 0 

for i in numbers :
    sum += int(i)

print(sum)

"""
실행결과 값
1 -> n = input() 의미없는 행 
23456 -> numbers = list(input()) 두번째줄에 숫자 입력하면 list로 아래 for문돌아서 아래 결과값 출력
20 -> print(sum)
"""