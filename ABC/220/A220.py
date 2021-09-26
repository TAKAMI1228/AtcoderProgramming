A, B, C = map(int, input().split())
i = 1
while C * i <= B:
    if A <= (C * i) <= B:
        print(C * i)
        break
    else:
        i = i + 1
if C * i > B:
    print(-1)
