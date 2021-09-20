N = int(input())
S = "A"
M = ""
while N > 1:
    if N % 2 == 0:
        N = N // 2
        M = M + "B"
    else:
        N = N - 1
        M = M + "A"
print(S + M[::-1])
