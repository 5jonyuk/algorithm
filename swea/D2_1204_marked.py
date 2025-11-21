from collections import Counter

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    point_List = list(map(int, input().split()))
    point_Count = Counter(point_List)

    # 카운터 객체를 배열로 변경 후 1번째 요소를 기준으로 정렬하고 0번째 요소로 정렬한 후 내림차순으로 변경
    result = sorted(point_Count.items(), key=lambda x: (x[1], x[0]), reverse=True)

    print(f"#{tc} {result[0][0]}")
