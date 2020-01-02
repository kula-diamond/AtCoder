N,A,B=map(int,input().split())
C=0
D=0

for i in range(1, N+1):
 C=0
 for j in str(i):
  C=C+int(j)
 if A<=C<=B:
  D=D+i

print(D)