#include<bits/stdc++.h>
#include <cstdio>
using namespace std;
#define for(i,a,b) for(int i=0;i<n;i++)

int peek(vector<int> a,int n){
    if(n==1) return a[0];
    int low=0,high=n-1;
    while(low<high){
        int mid=low+(high-low)/2;
        if(a[mid]>a[mid-1] and a[mid]>a[mid+1]) return a[mid];
        else if(a[mid]>a[mid-1] and a[mid]<a[mid+1]){
            low=mid+1;
            continue;
        }
        else{
            high=mid-1;
            continue;
        }
    }
    return -1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // std::ifstream input{"input.txt"};
    FILE *f1,*f2;
    f1=fopen("input.txt","r");
    f2=fopen("output.txt","w");

    int n; //number of elements in array
    fscanf(f1,"%d",&n);
    vector<int> a(n);
    for(i,0,n){
        fscanf(f1,"%d",&a[i]);
    }

    fprintf(f2,"Peek of the provided array is : %d",peek(a,n));
    return 0;
}