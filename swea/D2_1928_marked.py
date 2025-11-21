T = int(input())
for tc in range(1, T + 1):
    base_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    encord_s = input()
    full_binary, decord_s = "", ""

    for i in encord_s:
        full_binary += format(base_table.index(i), '06b')

    for i in range(0, len(full_binary), 8):
        decord_s += chr(int(full_binary[i:i + 8], 2))  # int 안에 2는 => 2진수로 해석해라

    print(f"#{tc} {decord_s}")
