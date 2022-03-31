from random import randint

def swap(A, i, j):
    t = A[i]
    A[i] = A[j]
    A[j] = t

def partition(A,p,q):
    pivot=A[q]
    i=p
    for j in range(p,q):
        if(A[j]<=pivot):
            swap(A,i,j)
            i+=1
    swap(A,i,q)
    return i

def randomised_partition(A, p, q): 
    id = randint(p, q)

    swap(A, id, q)
    return partition(A,p,q)


def randomised_select(A, p, q, i):
    if p == q and i > 1:
        print("error")
        return

    r = randomised_partition(A, p, q)
    k = r-p+1
    if(k == i):
        return A[r]
    elif i < k:
        return randomised_select(A, p, r-1, i)

    return randomised_select(A, r+1, q, i-k)

if __name__=="__main__":
    A= [2, 1, 7, 9, 6, 4, 8, 3]
    ans=randomised_select(A,0,len(A)-1,5)
    print(ans)
