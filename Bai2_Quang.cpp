#include<iostream>
using namespace std;

void main()
{
	int z = 0; //clear x
	int y = 0; //clear y
	int x;
	cin >> x;
	while (x != 0) // while x not 0 do
	{
		int temp = 0; //clear temp
		while (x != 0) //while x not 0 do
		{
			temp = temp + 1; //incr temp
			x = x - 1; //decr temp
		}//end
		while (temp != 0) //while temp not 0 do
		{
			x = x + 1; //incr x
			y = y + 1; //incr y
			temp = temp - 1; //decr temp
		}//end
		while (y != 0) //while y not 0 do
		{
			z = z + 1; //incr z
			y = y - 1; //decr y
		}//end
		x = x - 1; //decr x
	}//end
	cout << z << endl;
}