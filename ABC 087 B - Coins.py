# あなたは、500円玉をA枚、100円玉をB枚、50円玉をC枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうどX円にする方法は何通りありますか。
# A,B,C,X=(int(z) for z in input().split())
# A,B,C,X=map(int,'30 30 30 12000'.split())
A = int(input())
B = int(input())
C = int(input())
X = int(input())

N=0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i*500+j*100+k*50==X:
                N+=1

print(N)