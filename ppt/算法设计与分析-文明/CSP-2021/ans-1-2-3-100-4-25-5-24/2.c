#include<cstdio>
#include<algorithm>
#define maxn 100005
typedef long long LL;
using namespace std;
int n,N,a[maxn],R;
LL ans;
int main(){
	scanf("%d %d",&n,&N);
	for(int i=1;i<=n;++i)scanf("%d",&a[i]);
	a[n+1]=N;
	R=N/(n+1);
	for(int i=0;i<=n;++i){//a[i]~ a[i+1]-1
		int l=a[i],r=a[i+1]-1;
		l/=R,r/=R;
//		printf("%d %d\n",l,r);
		for(int j=l;j<=r;++j){//beishu
			ans+=abs(j-i)*(min((j+1)*R-1,a[i+1]-1)-max(j*R,a[i])+1);
//			printf("%d %d\n",max(j*R,a[i]),min((j+1)*R-1,a[i+1]-1));
		}
//		printf("%lld\n",ans);
	}
	printf("%lld",ans);
	return 0;
}