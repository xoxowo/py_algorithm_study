#1부터 12까지 8을 건너뛰고 출력하기 2
# if, countinue 문을 사용하지 않고 list 두개 더해서 

for i in list(range(1,8)) + list(range(9,13)) :
    print(i, end=' ')
print()