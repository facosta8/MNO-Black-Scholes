// librerias 
#include <iostream>
#include <fstream>
#include <string>
#include <vector> 
using namespace std;

int main () {
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
  cout << "desviacion estandar" << '\n';
  cout << valores[0] << '\n';
  cout << "el numero de betas es: ";
  cout << valores.size() - 2 << '\n'; 
  cout << "betas" << '\n';
  cout << valores[1] << '\n'; // no se por qué, pero la operacion agregar la desviacion estandar dos veces. Rarisimo.
  cout << valores[2] << '\n'; //beta 1
  cout << valores[3] << '\n';
  cout << valores[4] << '\n';
  cout << valores[5] << '\n';
  cout << valores[6] << '\n';
  cout << valores[7] << '\n';

  return 0;
}