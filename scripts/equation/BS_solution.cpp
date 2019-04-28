#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

double b5 = .21;

/*Definition of the function*/
double fn(double b0,double b1,double b2,double b3,double b4,double x)
{
	return b0 + b1*x + b2 *x*x + b3 *x*x*x + b4*x*x*x*x + b5*x*x*x*x*x;
}

/* The following lines are for the derivate approximation */
double d1(double b0,double b1,double b2,double b3,double b4,double x0,double h)
{
    return  (fn(b0,b1,b2,b3,b4,x0 + h) - fn(b0,b1,b2,b3,b4,x0 -h))/(2*h);
}

double d2(double b0,double b1,double b2,double b3,double b4,double x0,double h)
{
    return  ( fn(b0,b1,b2,b3,b4,x0 + h) - 2*fn(b0,b1,b2,b3,b4,x0) + fn(b0,b1,b2,b3,b4,x0 -h) ) / (h*h);
}

double d3(double b0,double b1,double b2,double b3,double b4,double x0,double h){
	return  ( fn(b0,b1,b2,b3,b4,x0 + 2*h) - fn(b0,b1,b2,b3,b4,x0 -2*h) - 2*( fn(b0,b1,b2,b3,b4,x0 + h) - fn(b0,b1,b2,b3,b4,x0 - h) ) )/ (2*h*h*h);
}

/*The 4th aproximation is not a good one, evaluate if we need a better one for the proyect o(h4 )*/
double d4(double b0,double b1,double b2,double b3,double b4,double x0,double h){
	return  ( fn(b0,b1,b2,b3,b4,x0 + 2*h) - 4*fn(b0,b1,b2,b3,b4,x0 + h) + 6*fn(b0,b1,b2,b3,b4,x0) - 4*fn(b0,b1,b2,b3,b4,x0 - h) + fn(b0,b1,b2,b3,b4,x0 - 2*h) )/ (h*h*h*h);
}

/*Calculate the integrate of the function*/

double in(double b0,double b1,double b2,double b3,double b4,double x0,double t){
    return 0;

}

int main(int argc, char** argv) {
	double b0 = 0,b1=0,b2=0,b3=0,b4=0;
	double x = 0;
	double result,result2, result3,result4;
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
	result3 = d3(b0,b1,b2,b3,b4,x,0.001);
	result4 = d4(b0,b1,b2,b3,b4,x,0.001);
	cout << "Resultado d1: " << result << ".\n";
	cout << "Resultado d2: " << result2 << ".\n";
	cout << "Resultado d3: " << result3 << ".\n";
	cout << "Resultado d4: " << result4 << ".\n";


	return 0;
}
