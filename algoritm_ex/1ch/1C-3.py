# 두자리 양수(10~99) 입력받기

print('2자리 양수를 입력하세요.')

while True :
    no = int(input('값을 입력하세요'))
    if no >= 10 and no <= 99 :  # 또는 10<= no <= 99 가능
                                # 드모르간의 법칙 적용시  if not(no < 10 or no >99)
        break
print(f'입력 받은 양수는 {no}입니다.')