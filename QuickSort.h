#include <iostream>
using namespace std;

template<class Type>
int Partition_1(Type Data[], int left, int right)    //第一种分割策略，将第一个元素作为哨兵，以右左顺序依次交换数据
{    //返回划分后轴元素对应的位置
	Type pivot = Data[left];  //选择最左边的为轴元素
	while (left < right)
	{
		while (left < right && Data[right] > pivot)
			right--;    //控制右指针移动
		Data[left] = Data[right];    //找到小数往左移动

		while (left < right && Data[left] <= pivot)
			left++;    //控制左指针移动
		Data[right] = Data[left];		//找到大数往右移动
	}
	Data[left] = pivot;		//此时left指向的位置为空，将轴元素放置于此
	return left;		//返回轴元素的新位置，实现分治
}

template<class Type>
int Partition_2(Type Data[], int start, int end)		//第二种分割策略，第一个元素作为哨兵待定，左右指针依次向前搜索
//遇到左大并且右小的情况，交换数据位置
{
	Type pivot = Data[start];		//选取第一个为哨兵
	int left = start, right = end;				//初始化left,right
	while (left <=right)		//外层控制遍历循环
	{
		while (left <= right && Data[left] <= pivot)	//控制左指针移动
			left++;
		while (left <= right && Data[right] > pivot) //控制右指针移动
			right--;
		if (left < right)
		{	//交换函数为内联函数，可以直接调用
			swap(Data[right], Data[left]);		
			right++;
			left--;
		}
	}
	//此时left指针位于right指针的右面，指向大于轴元素的数据，right与此相反
	swap(Data[start], Data[right]);	//交换轴元素与right指针所指的元素
	return right;		//返回轴元素新位置，实现分治
}


//此函数模板可以直接调用
//
//		By Xinjian Luo
//		2014/4/17
//	    http://blog.sina.com.cn/u/3640099785
template <class Type>
void QuickSort(Type Data[], int left, int right)		//此处left和right为数组下标（注意减一）
{	//用分治法实现
	if (left < right)  //控制结束条件
	{
		int p = Partition_1(Data, left, right);		//第一种分割策略
//		int p = Partition_2(Data, left, right);			//第二种分割策略
		QuickSort(Data, left, p - 1);		//左半面排序
		QuickSort(Data, p + 1, right);		//右半面排序
	}
}