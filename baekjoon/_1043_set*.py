import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth_person = list(map(int, input().split()))
truth_person_set = set(truth_person[1:])

party = [list(map(int, input().split())) for _ in range(m)]

while True:
    original_truth_person_num = len(truth_person_set)
    new_truth_person_num = original_truth_person_num
    next_party = []

    for p in party:
        know_truth = False
        for person in p[1:]:
            if (person in truth_person_set):
                know_truth = True
                break
        if (know_truth):
            truth_person_set.update(p[1:])
            new_truth_person_num = len(truth_person_set)
        else:
            next_party.append(p)

    party = next_party

    if (original_truth_person_num == new_truth_person_num):
        break


print(len(party))

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# knows = set(input().split()[1:])
# parties = [set(input().split()[1:]) for _ in range(M)]

# for _ in range(M):
#     for party in parties:
#         if party.intersection(knows):
#             knows = knows.union(party)

# cnt = 0

# for party in parties:
#     if party & knows:  # 교집합을 반환 즉 교집합이 있다면 다음 파티로 넘어감
#         continue
#     cnt += 1

# print(cnt)
