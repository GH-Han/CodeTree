A=list(map(int,input().split()))

for i in range(10):
    if i<2:
        print(A[i], end=" ")
    else:
        A.append((A[i-1]+A[i-2])%10)
        print(A[i],end=" ")



