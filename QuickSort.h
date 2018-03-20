#include <iostream>
using namespace std;

template<class Type>
int Partition_1(Type Data[], int left, int right)    //��һ�ַָ���ԣ�����һ��Ԫ����Ϊ�ڱ���������˳�����ν�������
{    //���ػ��ֺ���Ԫ�ض�Ӧ��λ��
	Type pivot = Data[left];  //ѡ������ߵ�Ϊ��Ԫ��
	while (left < right)
	{
		while (left < right && Data[right] > pivot)
			right--;    //������ָ���ƶ�
		Data[left] = Data[right];    //�ҵ�С�������ƶ�

		while (left < right && Data[left] <= pivot)
			left++;    //������ָ���ƶ�
		Data[right] = Data[left];		//�ҵ����������ƶ�
	}
	Data[left] = pivot;		//��ʱleftָ���λ��Ϊ�գ�����Ԫ�ط����ڴ�
	return left;		//������Ԫ�ص���λ�ã�ʵ�ַ���
}

template<class Type>
int Partition_2(Type Data[], int start, int end)		//�ڶ��ַָ���ԣ���һ��Ԫ����Ϊ�ڱ�����������ָ��������ǰ����
//�����������С���������������λ��
{
	Type pivot = Data[start];		//ѡȡ��һ��Ϊ�ڱ�
	int left = start, right = end;				//��ʼ��left,right
	while (left <=right)		//�����Ʊ���ѭ��
	{
		while (left <= right && Data[left] <= pivot)	//������ָ���ƶ�
			left++;
		while (left <= right && Data[right] > pivot) //������ָ���ƶ�
			right--;
		if (left < right)
		{	//��������Ϊ��������������ֱ�ӵ���
			swap(Data[right], Data[left]);		
			right++;
			left--;
		}
	}
	//��ʱleftָ��λ��rightָ������棬ָ�������Ԫ�ص����ݣ�right����෴
	swap(Data[start], Data[right]);	//������Ԫ����rightָ����ָ��Ԫ��
	return right;		//������Ԫ����λ�ã�ʵ�ַ���
}


//�˺���ģ�����ֱ�ӵ���
//
//		By Xinjian Luo
//		2014/4/17
//	    http://blog.sina.com.cn/u/3640099785
template <class Type>
void QuickSort(Type Data[], int left, int right)		//�˴�left��rightΪ�����±꣨ע���һ��
{	//�÷��η�ʵ��
	if (left < right)  //���ƽ�������
	{
		int p = Partition_1(Data, left, right);		//��һ�ַָ����
//		int p = Partition_2(Data, left, right);			//�ڶ��ַָ����
		QuickSort(Data, left, p - 1);		//���������
		QuickSort(Data, p + 1, right);		//�Ұ�������
	}
}