#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define EPS 1e-9
//#define RANDOM_MAX 10
typedef struct {
	int x;
	int y;
	int q;

}Point;
//三维函数，点是三维坐标。

typedef struct {
	Point point;
	int z;
}Abird;
//Abird结构体存放粒子的点和对应函数值的信息

typedef struct {
	Abird a[500];
}zuiyou;
//局部最优则建立一个zuiyou数组，全局最优建立一个zuiyou就可
//这里的500代表会放500个轮次的全局最优进去，所以500是轮次数。

int f(int x, int q,int r)//目标函数
{

	//return 2 * x * x * x + 3 * y * y * y + 4 * x * y * y - 5 * x * x * y + 10;
	return function(x,q,150-q,r);
}

Abird mymax(Abird bird[], int sz)//选择Abird作为返回值目的是返回整个带有完整信息(点，值)的最大值。
{
	Abird ret = bird[0];
	//printf("1");
	for (int i = 0; i < sz; i++)
	{
		if (ret.z - bird[i].z < EPS
			&& bird[i].point.x - 0.0 > EPS && 10.0 - bird[i].point.x > EPS
			&& bird[i].point.y - 0.0 > EPS && 10.0 - bird[i].point.y > EPS
			&& bird[i].point.q > 125  && 150 > bird[i].point.q)
        //控制粒子不要飞出界，飞出界的粒子我们就舍弃了
		{
			ret = bird[i];
		}
	}
	return ret;
}
int main(){return number(20);}
int number(int r)
{
	Abird bird[50] = { 0 };//50只鸟
	zuiyou jubu[50] = { 0 };//jubu[i].a[t]表示i鸟第t轮的局部最优
	zuiyou quanju = { 0 };//quanju.a[t]表示第t轮的全局最优
	Point v[50] = { 0 };//50只鸟速度矢量的创建
	srand((unsigned)time(NULL));//随机种子
	for (int i = 0; i < 10; i++)
	{
		//printf("1");
		bird[i].point.x = 1 + 1 * (rand() % 9) ;
		bird[i].point.q =137;
		//bird[i].point.y = 1 + 1 * (rand() % 9) ;
		//bird[i].point.q = 125 + 1 * (rand()% 25);
		v[i].x = 1 * (rand() % RAND_MAX) / RAND_MAX ;
		//v[i].y = 1 * (rand() % RAND_MAX) / RAND_MAX ;
		//v[i].q = 1 * (rand() % RAND_MAX) / RAND_MAX ;
	}//初始化50个粒子的速度和位置。
//随机生成[x, y)的浮点数，x ＋ 1.0 * ( rand() % RAND_MAX ) / RAND_MAX * ( y - x )
//随机生成[x,y]的浮点数，x ＋ 1.0 * rand() / RAND_MAX * ( y - x )

	for (int i = 0; i < 10; i++)
	{
		bird[i].point.x += v[i].x;
		//bird[i].point.y += v[i].y;
		//bird[i].point.q += v[i].q;
		bird[i].z = f(bird[i].point.x, bird[i].point.q,r);
		jubu[i].a[0] = bird[i];//第0轮的局部最优就是这次的位置
	}
	quanju.a[0] = mymax(bird, 50);
	//printf("%d",bird[0].z);
    //第0轮的全局最优
	int ti = 1;
	while (ti < 2)//进行499轮
	{
		for (int i = 0; i < 10; i++)
		{
            //更新速度
			v[i].x = 0.5 * v[i].x + 0.2 *  (jubu[i].a[ti - 1].point.x - bird[i].point.x) + 0.3 *  (quanju.a[ti - 1].point.x - bird[i].point.x);
			//v[i].y = 0.5 * v[i].y + 0.2 *  (jubu[i].a[ti - 1].point.y - bird[i].point.y) + 0.3 *  (quanju.a[ti - 1].point.y - bird[i].point.y);
			//v[i].q = 0.5 * v[i].q + 0.2 *  (jubu[i].a[ti - 1].point.q - bird[i].point.q) + 0.3 *  (quanju.a[ti - 1].point.q - bird[i].point.q);
            //更新位置
			bird[i].point.x += v[i].x;
			//bird[i].point.y += v[i].y;
			//bird[i].point.q += v[i].q;
			if(bird[i].point.x - 0.0 > EPS && R - bird[i].point.x > EPS)
			//&& bird[i].point.y - 0.0 > EPS && 10.0 - bird[i].point.y > EPS
			//&& bird[i].point.q > 125 && 150 > bird[i].point.q)
             //保证经过第t轮后出界的粒子被舍弃
			{
				bird[i].z = f(bird[i].point.x, bird[i].point.q,r);
			}
			else
			{
				bird[i].z = 0;
			}
			jubu[i].a[ti] = bird[i];//先把此次的局部最优储存起来
			jubu[i].a[ti] = mymax(jubu[i].a, ti + 1);//与历史过往的局部最优比较
		}
		quanju.a[ti] = mymax(bird, 50);//求第t轮的全局最优
		if (quanju.a[ti].z - quanju.a[ti - 1].z < EPS)
		{
			quanju.a[ti] = quanju.a[ti - 1];
		}//与上一轮的全局最优相比，若比上一轮差则交换。
		ti++;
		//printf("%d",quanju.a[ti - 1].z);
	}
	printf("%d,(%d,%d,%d)", quanju.a[ti - 1].z, quanju.a[ti - 1].point.x, quanju.a[ti - 1].point.x, quanju.a[ti-1].point.q);
	return 0;
}
struct Car{
	double x;//车的位置
	double bat;//车的电池量，这里放大6倍，总电量为600
    double sta;//车的状态与罚时
}car[125];

struct battaryA{
	double timemark;
}batA[150];

struct battaryB{
	double timemark;
}batB[150];

double dt = 0.1;
double t;
int x1=0;
int x2=0;//表示两个充电站位置，可以用double，不能取0/10
int answer = 0;//不能再用作全局变量
int numA2 = 125;//125-150
int numB2 = 25;//0-25
//printf("  ",x1,x2,numA2,numB2,answer);

//下边的不能改
int ini_num= 125;//初始发车数量
int ic;//车辆编号
int numA1 = 0;
int numB1 = 0;
int R=10;
float beta=1;

int function(int x,int numA_2,int numB_2,int R){
    x1=x;
    x2=x;
    numA2=numA_2;
    numB2=numB_2;
    R=R;
    beta=R/10;
    answer = 0;
    for (int i = 0; i < 125; i++)
    {
        car[i].x = R-x1*beta;
        car[i].bat = 600;
    }
    for (int i = 0; i < numA2; i++){
        batA[i].timemark = 0;
    }
    for (int i = 0; i < numB2; i++){
        batB[i].timemark = 0;
    }
    for (int i = 0; i < ini_num; i++)
    {
        car[i].sta = -3;//sta = -3表示进入发车状态
    }
    for (t = 0; t < 60000; t += dt)
    {
        update();
        //printf("%d      %d     %d     %d",x1,x2,numA2,numB2);
        printf("       %d\n",(int)t);
        //printf("%lf %lf %lf %d\n",car[0].x,car[0].sta,car[0].bat,answer);
        //printf("%d ",(int)car[1].x);
    }
    //printf("%d\n",answer);
    return answer;

}
//>0 fashi ==0 准备发车 =-1 正在运行 =-2 等待电池

void update(){
    for (ic = 0; ic < 125; ic++)
    {
        if (((car[ic].sta<1e-6&&car[ic].sta>-1e-6)||car[ic].sta==-3)&&judge(ic))
        {
            if(car[ic].sta==-3&&numA2>=0){
                numA2--;
            }
            car[ic].sta = -1;
            //numA2--;
        }

        if (car[ic].sta == -1||car[ic].sta == -2)//sta - 1表示 在运行
        {
        if(car[ic].sta==-1){
            if(car[ic].x<R&&car[ic].x>0)
            {
                car[ic].bat -= 2*dt;
            }else if(car[ic].x>R&&car[ic].x<2*R)
            {
                car[ic].bat -= 3*dt;
            }
            if (car[ic].x<1e-6||(car[ic].x-R>-1e-6&&car[ic].x-R<1e-6)||car[ic].x>2*R-(1e-6))
            {
                car[ic].sta = 1;
            }
            car[ic].x += 1*dt;
            if (car[ic].x>=2*R)
            {
                car[ic].x = car[ic].x - 2*R;
            }
            if(car[ic].x<1e-6) answer++;
        }
            checkcar(ic);//检车是否充电
        }
        if (car[ic].sta > 1e-6)//在罚时
        {
            car[ic].sta -= 1*dt;
        }

    }
    for (numA1=0; numA1 < numA2; numA1++)
    {
        batA[numA1].timemark -= 1*dt;
    }
    for (numB1=0; numB1 < numB2; numB1++)
    {
        batB[numB1].timemark -= 1*dt;
    }
}
void checkcar(int ic){
    //if(car[ic].bat<=76&&car[ic].bat>=60) printf("A");
    //if(car[ic].x-(10-x1)<1e-6&&car[ic].x-(10-x1)>-1e-6) printf("B");
    if (car[ic].bat<=99&&car[ic].bat>=60&&car[ic].x-(R-x1*beta)<1e-6&&car[ic].x-(R-x1*beta)>-1e-6)
    {
        //printf("A");
        if(car[ic].sta!=-2){
            numA2++;
            batA[numA2-1].timemark = 180;
        }
        //car[ic].sta = -2;
        if(batA[0].timemark<=0&&numA2>=0)
        {
            car[ic].bat = 600;
            //printf("B");
            car[ic].sta = 2;
            numA2--;
            changeA();
        }else{
            car[ic].sta = -2;
        }
    }
    if (car[ic].bat<=99&&car[ic].bat>=60&&car[ic].x-(R+x2*beta)<1e-6&&car[ic].x-(R+x2*beta)>-1e-6)
    {
        if(car[ic].sta!=-2){
        numB2++;
        batB[numB2-1].timemark = 180;
        }
        //car[ic].sta = -2;
        //printf("B");
        if (batB[0].timemark<=0&&numB2>=0)
        {
            car[ic].bat = 600;
            //printf("B");
            car[ic].sta = 2;
            numB2--;
            changeB();
        }else{
            car[ic].sta = -2;
        }
    }
}
void changeA(){
    for (int i = 0; i < numA2; i++)
    {
        batA[i].timemark = batA[i+1].timemark;
    }
}
void changeB(){
    for (int i = 0; i < numB2; i++)
    {
        batB[i].timemark = batB[i+1].timemark;
    }
}
//ic=9
int judge(int ic){
    int flag = 1;
    for (int i = 0; i < 125; i++)
    {
     if(i!=ic){
        if(car[ic].x-(10-x1*beta)<1e-6&&car[ic].x-(10-x1*beta)>-1e-6){
            if(car[i].sta==-1&&car[i].x>9.8-x1&&car[i].x<10.2-x1){
            flag = 0;}
        }
        if(car[ic].x - (10+x2*beta)<1e-6&&car[ic].x - (10+x2*beta)>-1e-6){
            if(car[i].sta==-1&&car[i].x>9.8+x2*beta&&car[i].x<10.2+x2*beta){
            flag = 0;}
        }
        if (car[ic].x<1e-6){
            if(car[i].sta==-1&&car[i].x<0.2)
            flag = 0;
        }
        if (car[ic].x - 10<1e-6&&car[ic].x - 10>-1e-6){
            if(car[i].sta==-1&&car[i].x<10.2&&car[i].x>9.8)
            flag = 0;
        }
        }
    }
    return flag;
}
