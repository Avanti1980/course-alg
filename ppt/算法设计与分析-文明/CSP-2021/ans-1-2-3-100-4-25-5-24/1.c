#include<cstdio>
#include<iostream>
#include<algorithm>
#define maxn 205
using namespace std;
int n,a[maxn],N;
long long ans;
int main(){
	scanf("%d %d",&n,&N);
	for(int i=1;i<=n;++i)scanf("%d",&a[i]);
	for(int i=1;i<n;++i){
		ans+=(a[i+1]-a[i])*i;
	}
	ans+=(N-a[n])*n;
	printf("%lld",ans);
	return 0;
}