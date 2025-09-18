import sys
input = sys.stdin.readline
n, m = map(int, input().split())

poketmon_by_number = {}
number_by_poketmon = {}

for i in range(n):
    poketmon = input().strip()
    poketmon_by_number[i+1] = poketmon
    number_by_poketmon[poketmon] = i+1

for _ in range(m):
    question = input().strip()
    if (question.isdigit()):
        # qestion을 정수형으로 변경해줘야함 위에 딕셔너리에서 정수로 저장했으니
        print(poketmon_by_number[int(question)])
    else:
        print(number_by_poketmon[question])
