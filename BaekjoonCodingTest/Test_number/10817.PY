A, B, C = map(int,input().split())

if A>B:
    if B>C:
        print(B)
    elif B<C:
        if A>C:
            print(C)
        elif A<C:
            print(A)
    elif B==C:
        print(B)
elif A<B:
    if B<C:
        print(B)
    elif B>C:
        if A>C:
            print(A)
        elif A<C:
            print(C)
    elif B==C:
        print(B)
elif A==B:
    if B>C:
        print(B)
    elif B<C:
        print(B)
    elif B==C:
        print(B)
