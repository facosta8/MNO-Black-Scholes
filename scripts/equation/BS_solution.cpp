#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>

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

double bs(double b0,double b1,double b2,double b3,double b4){

}



int main(int argc, char** argv) {
	double b0 = 0,b1=0,b2=0,b3=0,b4=0;
	double b5 = 0,b6=0.,b7=0.,b8=0.,b9=0.,b10=0.;
	double x = 0,t=0, sd = 0;
	double result,result2, result3,result4,result5;

	/*3##########################################
	##   Inicia proceso de carga de datos    ####
    #############################################*/

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

    valores.erase(valores.begin()); // eliminamos el primer elemento del vector, que queda con valor 0, ya que solo le fuimos agregando cosas
    valores.erase(valores.begin());
    sd = valores[0];
    t = valores[1];
    b1 = valores[2];
    b2 = valores[3];
    b3 = valores[4];
    b4 = valores[5];
    b5 = valores[6];
    b6 = valores[7];
    b7 = valores[8];
    b8 = valores[9];
    b9 = valores[10];
    b10 = valores[11];
    cout << sd << '\n';
    cout << t << '\n';
    cout << b1 << '\n';
    cout << b2 << '\n';
    cout << b3 << '\n';
    cout << b4 << '\n';
    cout << b5 << '\n';
    cout << b6 << '\n';
    cout << b7 << '\n';
    cout << b8 << '\n';
    cout << b9 << '\n';
    cout << b10 << '\n';


 	/*3##########################################
	############   B-S equation    ##############
    #############################################*/

	cout << "dame x: \n";
	cin  >> x;
	result = d1(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,0.001);
	result2 = d2(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,0.001);
	result3 = d3(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,0.001);
	result4 = d4(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,x,0.001);
	result5 = in(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,t);
	cout << "Resultado d1: " << result << ".\n";
	cout << "Resultado d2: " << result2 << ".\n";
	cout << "Resultado d3: " << result3 << ".\n";
	cout << "Resultado d4: " << result4 << ".\n";
	cout << "Resultado in: " << result5 << ".\n";


	return 0;
}
