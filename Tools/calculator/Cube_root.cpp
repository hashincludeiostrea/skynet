#include<iostream>
#include<cmath>
using namespace std; 
long double cuberoot(long double x );
int main ()
{
    system("clear"); 
    
long double number ; 
cout<<"\n\ncube(x) :: enter cube number  => "; 
cin>>number; 
 
cout<<"the cube number of "<<number<<" is => "<<cuberoot(number); 

}
long double cuberoot(long double x )
{
    return cbrt(x); 
}
