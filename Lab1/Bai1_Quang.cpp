#include<iostream>
using namespace std;

int main()
{
	int z;
	int x;
	cin >> x;
	z = 0; //clear z
	int y = 0; // clear y
	int temp = 0;//clear temp
	//gan x cho y
	while (x != 0) // while x not 0 do
	{
		temp = temp + 1; //incr temp
		x = x - 1; // decr x
	}//end
	while (temp != 0) //while temp not 0 do
	{
		temp = temp - 1; //decr temp
		x = x + 1; // incr x
		y = y + 1; // incr y
	}//end
	//thuc hien binh phuong giong nhu x*y vi ta da tao ra 1 bien y chua gia tri cua x
	while (x != 0) //while x not 0 do
	{
		int w = 0; //clear w
		while (y != 0) //while y not 0 do
		{
			z = z + 1; //incr z
			w = w + 1; //incr w
			y = y - 1; //decr y
		}//end
		while (w != 0) //while w not 0 do
		{
			y = y + 1; // incr y
			w = w - 1; // decr w
		}//end
		x = x - 1; //decr x
	}//end
	cout << z << endl;
}