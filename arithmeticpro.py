N,A,D=map(int,input().split())
x=0
for i in range (1,N+1):
    x=x+A
    A=A+D
print(x)    
