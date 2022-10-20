#include<stdio.h>
#define mod 929
char ch[10000];
int ss[2000];
int cnt;
int re[2000];
int xu[2000];
typedef struct
{
	int xu[2000];
	int len;
}HX;
int power(int a, int x)
{
	int re=1;
	while(x)
	{
		if(x&1)	re=(re*a)%mod;
		a=(a*a)%mod;
		x>>=1;
	}
	return re;
}
HX mul(HX a, HX b)
{
	HX c={{0}, 0};
	c.len=a.len+b.len-1;
	for(int i=0; i<a.len; i++)
	{
		for(int j=0; j<b.len; j++)
		{
			c.xu[i+j]+=a.xu[i]*b.xu[j];
		}
	}
	for(int i=0; i<c.len; i++)	c.xu[i]%=mod;
	return c;
}
HX m_mod(HX a, HX b)
{
	int ia=a.len-1;
	int ib=b.len-1;
	//int inv=power(b.xu[ib], mod-2);
	while(ia>=ib)
	{
		int cur=a.xu[ia]%mod;
		a.xu[ia]=0;
		ia--;
		for(int i=0; i<=ib-1; i++)
		{
			a.xu[ia-i]=(mod+a.xu[ia-i] - cur*b.xu[ib-1-i]%mod)%mod;
		}
		while(ia && a.xu[ia]==0) ia--;
	}	
	a.len=ia+1;
	return a;
}
HX getxu(int k, int ll)
{
	HX a={{0},1};
	a.xu[0]=1;
	HX b={{0}, 2};
	b.xu[1]=1;
	int cur=mod-1;
	for(int i=1; i<=k; i++)
	{
		cur=(3*cur)%mod;
		b.xu[0]=cur;
		a=mul(a,b);
		
		/*for(int i=0; i<a.len; i++)
		printf("%d ", a.xu[i]); //*/
	}
	for(int i=0; i<ll; i++)
	{
		b.xu[ll-1+k-i]=re[i];
	}
	b.xu[1]=b.xu[0]=0;
	b.len=ll+k;
	return m_mod(b,a);
}
int getmode(char c)
{
	if(c>='A' && c<='Z')	return 0;
	if(c>='a' && c<='z')	return 1;
	return 2;
}
int inputc(char c,int mode)
{
	if(mode==0)	return c-'A';
	if(mode==1)	return c-'a';
	return c-'0';
}
void work(void)
{
	int s=0,t;	//0大写，1小写，2数字
	int loc=0;
	while(ch[loc])
	{
		if(s==(t=getmode(ch[loc])))	ss[cnt++]=inputc(ch[loc],s);
		else
		{
			if(s==0)
			{
				if(t==1)	ss[cnt++]=27;
				else 	ss[cnt++]=28;
			}
			else if(s==1)
			{
				if(t==0)	ss[cnt++]=28,ss[cnt++]=28;
				else	ss[cnt++]=28;
			}
			else
			{
				if(t==0)	ss[cnt++]=28;
				else	ss[cnt++]=27;
			}
			s=t;
			ss[cnt++]=inputc(ch[loc],s);
		}
		loc++;
	} 
	if(cnt&1)	ss[cnt++]=29;
}
int main(void)
{
	
	int w,s;
	scanf("%d%d",&w,&s);
	scanf("%s",ch);
	work();
	cnt>>=1;
	for(int i=0; i<cnt; i++)
	{
		ss[i]=ss[i*2]*30+ss[i*2+1];
	}
	int k=0;
	if(s!=-1)
	{
		k=1;
		for(int i=0; i<=s; i++)	k<<=1;
	}
	int len=cnt+k+1;
	int pad=len%w;
	if(pad!=0)	pad=w-pad;
	int lens=pad+cnt+1;
	len+=pad;
	re[0]=lens;
	for(int i=1; i<=cnt; i++)	re[i]=ss[i-1];
	for(int i=1; i<=pad; i++)	re[i+cnt]=900;
	if(k==0)
	{
		for(int i=0; i<len; i++)	printf("%d\n",re[i]);
	}
	else
	{
		HX c=getxu(k, lens);
		for(int i=0; i<k; i++)	c.xu[i]=(mod-c.xu[i])%mod;
		for(int i=1; i<=k; i++)	re[i+pad+cnt]=c.xu[k-i];
		for(int i=0; i<len; i++)	printf("%d\n",re[i]);
	}
	return 0;
}