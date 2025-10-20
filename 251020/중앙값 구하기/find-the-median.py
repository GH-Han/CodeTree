A,B,C = map(int,input().split())

if A > B:
    if B >C:
        print(B)
    elif A>C:
        print(C)
    else:
        print(A)
        # A<B
else:
    if B<C:
        print(B)
    elif A>C: #C<B
        print(A)
    else:
        print(C)
        
    