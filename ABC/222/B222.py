N, P = map(int, input().split())
a = list(map(int, input().split()))
huka = 0
for i in range(N):
    if a[i] < P:
        huka += 1
print(huka)
