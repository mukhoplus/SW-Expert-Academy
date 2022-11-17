# SW Expert Academy 15230: 알파벳 공부(D3)
T = int(input())

for test_case in range(1, T + 1):
    S = input()
    answer = 0
    for i in range(len(S)):
        if ord(S[i]) != 97 + i:
            break
        answer += 1
print('#' + str(test_case) + ' ' + str(answer))