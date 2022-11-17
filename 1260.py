# SW Expert Academy 1206: [S/W 문제해결 기본] 1일차 - View(D3)
def calc(lst):
    temp = lst[:2] + lst[3:]
    result = lst[2] - max(temp)
    if result < 0:
        return 0
    return result

def main():
    for test_case in range(1, 11):
        N = int(input())
        land = list(map(int, input().split()))
        answer = 0
        for i in range(2, N-2):
            answer += calc(land[i-2:i+3])
        print('#' + str(test_case) + ' ' + str(answer))

main()