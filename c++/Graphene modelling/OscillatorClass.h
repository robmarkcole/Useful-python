// Oscillator class file - USES KIPPENBERG NATURE PHYS SUPPLEMENTARY EQUATION S7 TO CALCULATE g0
#ifndef OSCILLATORCLASS_H
#define OSCILLATORCLASS_H

#include <iostream>
#include "constants.h"	
#include "functions.h"

////////////// Base class
class Oscillator {
		public: // make everything public
		double Omega_m, mass_ef, Q_m;    // has these properties
		Oscillator (double, double, double); // constructor must have same name as class NEEDED
		double Gamma_m () { return (Omega_m/Q_m) ;}          //function that can be called, returns rads
		double x_zpf () {return(sqrt(hBar/(2*mass_ef*Omega_m)));}        // zero point motion
};
Oscillator::Oscillator(double a, double b, double c) //constructor 
{Omega_m=a; mass_ef=b; Q_m = c;  
};

///////////// Sub classes KNOWN g0 eg plasmon
class OscillatorKnown_g0 : public Oscillator {   //sub class with known g0 eg plasmon
		public:
		double g0;
		OscillatorKnown_g0(double, double, double, double); //constructor
		double g0_val (){return g0;}
};
OscillatorKnown_g0::OscillatorKnown_g0(double a, double b, double c, double d)
	:Oscillator(a, b, c) //inherits and uses constructor
	{
		g0 = d;  // take Hz/m
};


///////////// Sub classes SHEET to calculate g0
class OscillatorSheet : public Oscillator {   //sub class with known g0 eg plasmon
		public:
		double sample_length_y, sample_length_x, V_cav, alpha, thickness, Omega_cav, CC, AA, BB, g0;
		OscillatorSheet(double, double, double, double, double, double, double, double, double, double); //constructor
		double g0_val (){return g0;}
};
OscillatorSheet::OscillatorSheet(double a, double b, double c, double d, double e, double f, double g, double h, double i, double j)
	:Oscillator(a, b, c) //inherits and uses constructor
	{
		sample_length_y = d; sample_length_x = e; V_cav = f; alpha = g; thickness = h; Omega_cav = i; CC=j;
		AA=sample_length_y*sample_length_x/V_cav; // unit less
		BB=(1-exp(-2*alpha*thickness))/(2*alpha);
		g0 = Omega_cav*alpha*AA*BB*CC;

};

///////////// Sub classes STRING to calculate g0
class OscillatorString : public OscillatorSheet {   //sub class with known g0 eg plasmon
		public:
		double string_width, Tor_radius;
		OscillatorString(double, double, double, double, double, double, double, double, double, double, double, double); //constructor
		//double g0_val (){return g0;}
};
OscillatorString::OscillatorString(double a, double b, double c, double d, double e, double f, double g, double h, double i, double j, double k, double l)
	:OscillatorSheet(a, b, c, d, e, f, g, h, i, j) //inherits and uses constructor
	{
		string_width = k;
		Tor_radius = l;
		//AA=string_width*sample_length_x/V_cav;        // this is for a vertically aligned string
		AA=string_width*sqrt(pi*Tor_radius/alpha)/V_cav;// this is for a vertically aligned string
		BB=(1-exp(-2*alpha*thickness))/(2*alpha); // as in paper
		g0 = Omega_cav*alpha*AA*BB*CC;
};

#endif
