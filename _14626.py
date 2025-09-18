# isbn = input()
# isbn_list = []
# isbn_list_sum = 0
# multione = 1
# multithree = 3
# targetIndex = 0

# for item in isbn:
#     isbn_list.append(item)

# if (isbn_list[12] == '*'):
#     for i in range(12):
#         if (i % 2 == 0):
#             isbn_list_sum += int(isbn_list[i])*1
#         else:
#             isbn_list_sum += int(isbn_list[i])*3
#     isbn_list[12] = 10 - isbn_list_sum % 10
#     print(isbn_list[12])

# else:
#     for i in range(13):
#         if (i % 2 == 0):
#             if (isbn_list[i] == '*'):
#                 targetIndex = i
#                 continue
#             isbn_list_sum += int(isbn_list[i])*1
#         else:
#             if (isbn_list[i] == '*'):
#                 targetIndex = i
#                 continue
#             isbn_list_sum += int(isbn_list[i])*3
#     if (targetIndex % 2 == 0 or targetIndex == 0):
#         isbn_list[targetIndex] = multione
#     else:
#         isbn_list[targetIndex] = multithree

#     for k in range(10):
#         if ((isbn_list_sum + k*isbn_list[targetIndex]) % 10 == 0):
#             break
#         print(k)

isbn = input()

for i in range(10):
    partial_sum = 0
    for j in range(13):
        if (isbn[j] == '*'):
            weight = 1 if j % 2 == 0 else 3
            partial_sum += weight * i
        else:
            weight = 1 if j % 2 == 0 else 3
            partial_sum += int(isbn[j])*weight
    if (partial_sum % 10 == 0):
        print(i)
        break
