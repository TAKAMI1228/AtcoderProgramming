N = int(input())
Ai = [] * N
As = [] * N
Ai = list(range(1, N + 1))
As = list(map(int, input().split()))
Adict = dict(zip(Ai, As))
Ads = sorted(Adict.items(), key=lambda i: i[1], reverse=True)
print(Ads[1][0])
