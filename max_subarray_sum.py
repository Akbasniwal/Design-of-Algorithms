def max_crrosing_subarray(A,l,h,mid):
    k=mid
    summ,sleft,sright=0,0,0
    i,j=mid,mid+1
    left,right=mid,mid+1
    while(i>=0):
        summ+=A[i]
        if summ > sleft:
            sleft=summ
            left=i
        i-=1
    summ=0
    while(j<=h):
        summ+=A[j]
        if summ >sright:
            sright=summ
            right=j
        j+=1
    return (left,right,sleft+sright)

def max_subarray(A,l,h):
    m=(h+l)//2
    if l==h:
        return (l,h,A[l])
    (ll,lr,ls)=max_subarray(A,l,m)
    (rl,rr,rs)=max_subarray(A,m+1,h)
    (cl,cr,cs)=max_crrosing_subarray(A,l,h,m)

    if(ls >=rs and ls>=cs):
        return (ll,lr,ls)
    elif(rs>=ls and rs>=cs):
        return (rl,rr,rs)
    else:
        return (cl,cr,cs)

if __name__=="__main__":
    A=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    ans=max_subarray(A,0,len(A)-1)
    print("\nmax subarray sum is {} between the indices i={} and j={}\n".format(ans[2],ans[0],ans[1]))
