def max_crrosing_subarray(A,l,h,mid):
    k=mid
    summ,sleft,sright=0,0,0
    i,j=mid,mid+1
    while(i>=0):
        summ+=A[i]
        if summ > sleft:
            sleft=summ
        i-=1
    summ=0
    while(j<=h):
        summ+=A[j]
        if summ >sright:
            sright=summ
        j+=1
    return sleft+sright

def max_subarray(A,l,h):
    m=(h+l)//2
    if l==h:
        return A[l]
    max_lr=max(max_subarray(A,l,m),max_subarray(A,m+1,h))
    return max(max_lr,max_crrosing_subarray(A,l,h,m))

if __name__=="__main__":
    A=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print(max_subarray(A,0,len(A)-1))
