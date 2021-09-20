A,B=map(int,input().split())
if 0<A and B==0:
    print("Gold")
elif 0<B and A==0:
    print("Silver")
elif 0<A and 0<B:
    print("Alloy")