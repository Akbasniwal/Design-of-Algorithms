def peek(A,l,h):
    if(l==h):
        return A[l]
    m=(h+l)//2
    if(A[m]>A[m-1] and A[m]>A[m+1]): #if left and right both are less means A[m] is the peek
        return A[m]
    elif A[m]>A[m-1] and A[m]<A[m+1]:
        return peek(A,l,m)
    else:
        return peek(A,m+1,h)

A=[1,2,3,6,8,5,4,2,1]
print(peek(A,0,len(A)-1))
# Time complexiety - O(logn)
