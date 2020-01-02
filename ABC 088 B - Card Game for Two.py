N = int(input())
A = list(map(int, input().split()))

# A = [20,18,2,18]
Alice = 0
Bob = 0

A.sort(reverse=True)

for i,num in enumerate(A):
    if i%2 == 0:
        Alice+=num
    else:
        Bob+=num

print(Alice-Bob)