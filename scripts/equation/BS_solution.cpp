#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <math.h>

using namespace std;


/*Definition of the function*/
double fn(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x)
{
	return b0 + b1*x + b2 *x*x + b3 *x*x*x + b4*x*x*x*x + b5*x*x*x*x*x + b6*x*x*x*x*x*x + b7*x*x*x*x*x*x*x + b8*x*x*x*x*x*x*x*x + b9*x*x*x*x*x*x*x*x*x + b10*x*x*x*x*x*x*x*x*x*x;
}

/* The following lines are for the derivate approximation */
double d1(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x0,double h)
{
    return  (fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 + h) - fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 -h))/(2*h);
}

double d2(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x0,double h)
{
    return  ( fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 + h) - 2*fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0) + fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 -h) ) / (h*h);
}

double d3(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x0,double h){
	return  ( fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 + 2*h) - fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 -2*h) - 2*( fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 + h) - fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 - h) ) )/ (2*h*h*h);
}

/*The 4th approximation is not a good one, evaluate if we need a better one for the project o(h4 )*/
double d4(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x0,double h){
	return  ( fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 + 2*h) - 4*fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 + h) + 6*fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0) - 4*fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 - h) + fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0 - 2*h) )/ (h*h*h*h);
}

/*Calculate the integrate of the function by trapezoidal rule*/

double in(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double t){
    int n = 100,i;
    double h = t/n,sum=0,x0=0;
    for(i = 1;i <= n-1;i++){
        x0= x0 + h;
        sum = sum + fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x0);
    }
    return (t/(2*n))*(fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,0) + fn(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,t) + 2*sum );

}

double u0(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x){
    return fn( b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x);
}

double A0(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x){
    return (d2( b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01))*d2( b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01);
}

double u1(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x,double t,double sd, double ro, double r){
    return -1*(-0.5*sd*sd*x*x*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01) + r*x*d1(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)-r)*t + ro*sd*sd*x*x*x*A0(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x)*t;
}

 double A1(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x,double t,double sd, double ro, double r){
    return 2*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)*(-1*(-0.5*sd*sd*(2*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+x*x*d4(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+r*x*d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)))*t + (ro*sd*sd*t*6*x*(2*(d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)*d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+d4(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01) ))));
 }

 double u2(double b0,double b1,double b2,double b3,double b4,double b5,double b6,double b7,double b8,double b9,double b10,double x,double t,double sd, double ro, double r){
    return -1*(-0.5*sd*sd*x*x*((-1*(-0.5*sd*sd*(2*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+x*x*d4(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+r*x*d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)))*t + (ro*sd*sd*t*6*x*(2*(d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)*d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+d4(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01) ))))) + r*x*(-1*(-0.5*sd*sd*(2*x*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+x*x*d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)) + r*(d1(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)+x*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)))*t + ro*sd*sd*t*(3*x*x*A0(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x) + x*x*x+(2*d2(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01)*d3(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,b10, x,0.01))))-r)*t + ro*sd*sd*t*x*x*x*A1(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,t,sd,ro,r);
 }
int main(int argc, char** argv) {
	double b0 = 0,b1=0,b2=0,b3=0,b4=0;
	double b5 = 0,b6=0.,b7=0.,b8=0.,b9=0.,b10=0.;
	double x = 0,t=0, sd = 0,ro = -0.9,r = 0.18;
	double result,result2, result3,result4,result5,resultado = 0.0;

	/*3##############################################################
	##   Inicia proceso de carga de datos y se asignan valores   ####
    #################################################################*/

    vector<double> valores;
    double valor;
    string line;
    ifstream myfile ("data.txt");

    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            if (line[0] != '#')
                //cout << line << '\n';
                valor = atof(line.c_str());
                valores.emplace_back(valor);
        }
        myfile.close();
    }
    else cout << "¡NOOOOO! ¡El archivo no existe!";

    //valores.erase(valores.begin()); // eliminamos el primer elemento del vector, que queda con valor 0, ya que solo le fuimos agregando cosas
    //valores.erase(valores.begin());
    sd = valores[0];
    x = valores[1]/valores[1]; /* Valor al último día*/
    t = valores[2]/12; /* tiempo que dura*/
    b0 = valores[3];
    b1 = valores[4];
    b2 = valores[5];
    b3 = valores[6];
    b4 = valores[7];
    b5 = valores[8];
    b6 = valores[9];
    b7 = valores[10];
    b8 = valores[11];
    b9 = valores[12];
    b10 = valores[13];

   	/*###########################################
	############   B-S equation    ##############
    #############################################*/

	result = u0(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x);
	result2 = A0(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x);
	result3 = u1(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,t,sd,ro,r);
	result4 = A1(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,t,sd,ro,r);
	result5 = u2(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,t,sd,ro,r);
	resultado = result + result3 + result5; /*Suma de terminos para aproximación de resultados*/
	/*cout << "Resultado u0: " << result << ".\n";
	cout << "Resultado A0: " << result2 << ".\n";
	cout << "Resultado u1: " << result3 << ".\n";
	cout << "Resultado A1: " << result4 << ".\n";
	cout << "Resultado u2: " << result5 << ".\n";
	cout << "Resultado u(" << x << "," << t << "):   " << resultado << "\n";*/
    cout << resultado;


	return 0;
}
