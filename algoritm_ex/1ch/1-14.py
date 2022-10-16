from tkinter import W


n = int(input('몇 개를'))
w = int(input('몇 개마다'))

for _ in range(n//w):
    print('*'* w)

rest = n % W
if rest :
    print('*' * rest)
