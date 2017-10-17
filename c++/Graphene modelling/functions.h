#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <cmath>	
#include <iostream>	
#include "constants.h"

// Functions all //////////////////////////////////////////////////////////////////////////////////////
double Hz2Rad_FUNC(double Hz){      //convert a Hz value to rads
	double Hz2Rad=2*pi*Hz;
	return Hz2Rad; 
};

double max_double(double a, double b){ // return the largest of two doubles
	double output;
	if(a>b)
	output=a;
	else
	output = b;
	return output;
}

double g0_to_MHz_nm(double g0){ //take in Hz/m
	return g0/(1e15); 
}

#endif