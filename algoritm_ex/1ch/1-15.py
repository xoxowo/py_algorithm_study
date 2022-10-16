# *을 n개 출력하되 w개마다 줄바꿈 하기 2

n =int(input('출력할 *의 개수를 입력하세요. :'))
w =int(input('줄바꿈 위치를 입력하세요. :'))

for _ in range (n//w) :
    print ('*' * w )

rest = n % w
if rest :
    print ('*' * rest)