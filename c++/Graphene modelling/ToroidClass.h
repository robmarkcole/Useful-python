// ToroidClass.h class file by Robin. For a microsphere just set Small_radius = Tor_radius, add funciton to instantiate a test toroid and print out
#ifndef TOROIDCLASS_H
#define TOROIDCLASS_H

#include <cmath>		
#include "constants.h"

class Toroid {
		public: 
		double Tor_radius, Small_radius, D_mode, f_r, coupling, Q_opt, n_toroid, n_dielectric, wavelength, alpha, sample_length_y, sample_length_x;  
		Toroid(double, double, double, double, double, double, double, double, double); //constructor
		// Methods
		double mode_area () { return (2*pi*Tor_radius*D_mode) ;}          //function that can be called, unit area
		double Kappa (double Omega_cav) {return(Omega_cav/Q_opt);}        // Optical linewidth rads
		double V_cav () {return (2*Tor_radius*pow(pi,2)*pow(D_mode/2,2));}// return mode volume
};
// constructor
Toroid::Toroid(double a, double b, double c, double d, double e, double f, double g, double h, double i)
{Tor_radius=a; Small_radius=b; D_mode=c; f_r = d; coupling = e; Q_opt = f; n_toroid = g; n_dielectric =h; wavelength = i;

alpha= (pow(n_toroid,2) -1)/(wavelength*n_dielectric/(2*pi)); // unit m^-1 decay distance?
sample_length_y = pow(pi*Tor_radius/alpha,0.5);     //length sampled along toroid large radius, m
sample_length_x = pow(pi*Small_radius/alpha,0.5);   // length sampled along toroid large radius, m
}; 

#endif