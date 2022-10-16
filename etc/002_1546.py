n = input()
score = list(map(int, input().split()))
avg = sum(score) * 100 / max(score) / int(n)

print(avg)

"""
실행결과 값
2  ->총 몇개의 과목이 입력하는 행
3 10 -> 2과목의 각 점수 입력 
65.0 -> 입력된 과목의 합 *100 / 최고점수 / 나누기 과목 수 
"""