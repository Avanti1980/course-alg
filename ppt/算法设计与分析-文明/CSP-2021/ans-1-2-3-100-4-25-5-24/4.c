#include<cstdio>
#define maxm 10005
int n,m,k,op;
int id,l,r,x;
int a[maxm],b[maxm];
int vis[maxm],last[maxm];
int main(){
	scanf("%d %d %d",&n,&m,&k);
	while(k--){
		int op;
		scanf("%d",&op);
		if(op==0){
			scanf("%d %d %d %d",&id,&l,&r,&x);
			int ans=-1;
			for(int i=l;i<=r;++i){
				if(!b[i])a[i]=x,b[i]=id,ans=i;
				else if(b[i]==id)a[i]=x,ans=i;
				else break;
			}
			printf("%d\n",ans);
		}
		if(op==1){
			scanf("%d %d %d",&id,&l,&r);
			bool flag=1;
			for(int i=l;i<=r;++i){
				if(b[i]!=id){flag=0;break;}
			}
			if(flag){
				for(int i=l;i<=r;++i){
					last[i]=b[i],vis[i]=a[i];
					b[i]=a[i]=0;
				}
			}
			printf(flag?"OK\n":"FAIL\n");
		}
		if(op==2){
			scanf("%d %d %d",&id,&l,&r);
			bool flag=1;
			for(int i=l;i<=r;++i){
				if(b[i]||last[i]!=id){flag=0;break;}
			}
			if(flag){
				for(int i=l;i<=r;++i){
					b[i]=last[i],a[i]=vis[i];
					last[i]=vis[i]=0;
				}
			}
			printf(flag?"OK\n":"FAIL\n");
		}
		if(op==3){
			scanf("%d",&l);
			if(b[l])printf("%d %d\n",b[l],a[l]);
			else printf("0 0\n");
		}
	}
	return 0;
}