import numpy as np

N = int(input())
A = np.array([int(i) for i in input().split()])

def check_even(A, B):
    odd_flag=0
    while odd_flag!=1:
        for i, num in enumerate(A):
            if num%2 == 1:
                odd_flag=1
                break
            elif i==len(A)-1:
                A=A/2
                B+=1
    return B

def main():
    print(check_even(A, 0))

if __name__ == '__main__':
    main()