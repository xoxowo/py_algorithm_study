# 1~99 사이의 난수 n개 생성하기 (13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요'))

for _ in range(n):
    r = random.randint (1, 99)
    print(r, end=' ')
    if r == 13 :
        print('\n 13이 나와 프로그램을 중단합니다.')
        break
else :
    print ('\n 난수 생성을 종료합니다.')    