S = [] * 3
Sp = ""
for i in range(3):
    S.append(input())
T = input()
for j in range(len(T)):
    Sp = Sp + S[int(T[j]) - 1]
print(Sp)
