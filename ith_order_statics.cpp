#include<bits/stdc++.h>
using namespace std;

int partition(int A[],int p,int q){
    int x = A[q], i = p;
    for (int j = p; j <= q - 1; j++)
    {
        if (A[j] <= x)
        {
            swap(A[i], A[j]);
            i++;
        }
    }
    swap(A[i], A[q]);
    return i;
}

int randomize_partition(int A[],int p,int q){
    int id=rand()%(q-p+1)+p;
    swap(A[id],A[q]);
    return partition(A,p,q);
}

int randomize_select(int A[],int p,int q,int i){
    if(p==q and i>1) {
        cout<<"error"<<endl;
        return -1;
    }

    else{
        int r=randomize_partition(A,p,q);
        int k=r-p+1;
        if(k==i) return A[r];
        else if(k >i){
            return randomize_select(A,p,r-1,i);
        }
        return randomize_select(A,r+1,q,i-k);
    }
}

int main(){
    int A[]={8,7,9,64,8,6,5,4,2,33};
    int n=sizeof(A)/sizeof(A[0]);

    int ans=randomize_select(A,0,n-1,5);
    cout<<ans<<endl;
    return 0;
}