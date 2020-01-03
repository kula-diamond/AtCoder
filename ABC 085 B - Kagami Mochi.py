N = int(input())
d = [int(input()) for j in range(N)]

# d = [1,2]

d.sort(reverse=True)

current_mochi = 0
next_mochi = 0
counter = 0

for i,num in enumerate(d):
    next_mochi = num
    if i == 0:
        counter+=1
        current_mochi = num
    elif i + 1 == len(d):
        if current_mochi > next_mochi:
            counter+=1
            break
        else:
            break
    elif current_mochi > next_mochi:
        counter+=1
        current_mochi = num

print(counter)