#include<bits/stdc++.h>
#define LL long long
using namespace std;
LL read(){
	LL x=0,w=1;char ch=getchar();
	while(ch>'9'||ch<'0'){if(ch=='-')w=-1;ch=getchar();}
	while(ch>='0'&&ch<='9')x=(x<<3)+(x<<1)+ch-48,ch=getchar();
	return x*w;
}
LL n,k1,k2;
LL cnt,head[500010],du[500010];
struct node{
	LL to,next;
}edge[1000010];
void add(LL x,LL y){
	cnt++;edge[cnt].next=head[x];edge[cnt].to=y;head[x]=cnt;
}
LL ans1,vis1[5010];
void dfs1(LL k,LL root,LL maxx,LL minn){
	vis1[k]=1;
	for(LL i=head[k];i;i=edge[i].next){
		LL v=edge[i].to;if(vis1[v])continue;
		if(k==root){
			ans1++;
			dfs1(v,k,max(root,v),min(root,v));
		}
		else{
			if(min(root,v)-k1<=minn&&maxx<=max(root,v)+k2){
				ans1++;
			}
			dfs1(v,root,max(maxx,v),min(v,minn));
		}
	}
}
void work1(){
	LL ans=0;
	for(LL i=1;i<=n;i++){
		for(LL j=1;j<=n;j++)vis1[j]=0;
		ans1=0;
		dfs1(i,i,0,0);
		ans+=ans1;
	}
	printf("%lld\n",ans/2+n);
}
void work2(){
	
}
void work3(LL k){
	LL ans3=n+n-1;
	for(LL i=1;i<=n;i++){
		if(i==k)continue;
		if(i<k){
			ans3+=k-max(i+1,k-k2);
			ans3+=(n-k);
		}
		else {
			if(i-k1<=k)ans3+=n-i;
		}
	}
	printf("%lld\n",ans3);
}
int main(){
	n=read();k1=read();k2=read();
	for(LL i=1;i<n;i++){
		LL x=read(),y=read();
		du[x]++;du[y]++;
		add(x,y);add(y,x);
	}
	if(n<=5000){work1();return 0;}
	LL flag2=0,flag3=0;
	for(LL i=1;i<=n;i++){
		if(du[i]>2)flag2=1;
		if(du[i]==n-1)flag3=i;
	}
	if(flag2)work2();
	if(flag3)work3(flag3);
}