A,B=map(int,input().split())
S="Alloy"
if 0<A and B==0:
    S="Gold"
elif 0<B and A==0:
    S="Silver"
print(S)