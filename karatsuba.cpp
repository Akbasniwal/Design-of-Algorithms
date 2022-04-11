//Multiplying two big numbers using karatsuba algorithm(divide and conquer approach)
#include<bits/stdc++.h>
#include <cstdio>
#include <sstream>
using namespace std;
#define for(i,a,b) for(int i=0;i<n;i++)
typedef long long int ll; 

ll multi(ll x,ll y){
    stringstream ss,ss1;
    string s;
    ss<<x;
    ss>>s;
    int l1=s.length();
    ss1<<y;
    ss1>>s;
    int l2=s.length();
    
    int d=max(l1,l2)/2;
    ll x1=x/pow(10,d);
    ll x0=x % (ll)pow(10,d);
    ll y1=y / pow(10,d);
    ll y0=y % (ll)pow(10,d);

    ll x0y0=x0*y0;
    ll x1y1=x1*y1;
    ll x1y0_x0y1=(x0+x1)*(y0+y1)-x0y0-x1y1;
    return x1y1*pow(10,2*d)+x1y0_x0y1*pow(10,d)+x0y0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // std::ifstream input{"input.txt"};
    FILE *f1,*f2;
    f1=fopen("input.txt","r");
    f2=fopen("output.txt","w");
    ll x,y;
    fscanf(f1,"%lld %lld",&x,&y);
    fprintf(f2,"%lld",multi(x, y));
    return 0;
}