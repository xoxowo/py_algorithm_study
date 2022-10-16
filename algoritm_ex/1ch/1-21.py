#구구단 곱셈

n = int(input('출력하고 싶은 단의 숫자를 입력하세요'))

for i in range(n, 10) :
    print(f'{n} x {i} = {n*i}')

#구구단 전체 출력 시

print()
print('2부터 9까지 구구단을 출력합니다.')


for a in range(2, 10) :
    for j in range(1, 10) :
        print(f'{a} x {j} = {a*j}')
    print('--------------')

