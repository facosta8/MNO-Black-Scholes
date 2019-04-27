#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

double fn(double b0,double b1,double b2,double b3,double b4,double x)
{
	return b0 + b1*x + b2 *x*x + b3 *x*x*x + b4*x*x*x*x;
}

double d1(double b0,double b1,double b2,double b3,double b4,double x0,double h)
{
    return  (fn(b0,b1,b2,b3,b4,x0 + h) - fn(b0,b1,b2,b3,b4,x0 -h))/(2*h);
}

double d2(double b0,double b1,double b2,double b3,double b4,double x0,double h)
{
    return  ( fn(b0,b1,b2,b3,b4,x0 + h) - 2*fn(b0,b1,b2,b3,b4,x0) + fn(b0,b1,b2,b3,b4,x0 -h) ) / (h*h);
}


int main(int argc, char** argv) {
	double b0,b1,b2,b3,b4;
	double x;
	double result,result2;
	cout << "dame b0: \n";
	cin  >> b0;
	cout << "dame b1: \n";
	cin  >> b1;
	cout << "dame b2: \n";
	cin  >> b2;
	cout << "dame b3: \n";
	cin  >> b3;
	cout << "dame b4: \n";
	cin  >> b4;
	cout << "dame x: \n";
	cin  >> x;
	result = d1(b0,b1,b2,b3,b4,x,0.001);
	result2 = d2(b0,b1,b2,b3,b4,x,0.001);
	cout << "Resultado d1: " << result << ".\n"; 
	cout << "Resultado d2: " << result2 << ".\n"; 
	
	return 0;
}
