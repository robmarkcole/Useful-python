#include <iostream>
#include <cmath>
#include <iomanip>





using namespace std;
int main(int argc, char *argv[]) {
	double a = 1.93414e+06;
	double b = 320; 
	cout << fixed << setprecision(1) << max(a,b) << endl; ;
	//cout << floor(a);
	return 0;
}