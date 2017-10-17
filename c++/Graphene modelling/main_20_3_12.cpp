// TO USE Input desired variables, got to Main() and comment in correct Resonator Instantiator

#include <iostream>
#include <cmath>
#include "OscillatorClass.h"
#include "ToroidClass.h"
#include "functions.h"
using namespace std;

////////////// Toroid and experiment Variables ENTER
double Q_opt = 1e8; // Optical Q
double Tor_radius = 30e-6; // toroid major radius, m
double Small_radius = 3e-6; // toroid minor radius, m
double D_mode = 3.5e-6; // diameter of toroid optical mode
double f_r = 0.4; // field at toroid rim

double coupling = 1; // Nu_c coupling parameter, set 1
double x0=0; // location of beam start with respect to toroid rim, 0 for our calculations

double n_toroid = n_silica;
double n_resonator = n_Graphene; // mechanical resonator
double n_dielectric = n_air;
//double n_dielectric = 1.3;
double wavelength = 1550e-9;//m

double Omega_cav = (2*pi*c)/(wavelength); //rads in free space

//  Resonator properties ENTER
//int    resonator_type = 1; //type 1 for AFM cantilever or plasmon with known g0, 2 for beam sheet where calculate g0
double Omega_m = Hz2Rad_FUNC(7e7); // mechanical freq, accepts Hz
double mass_ef = 10*1.22e-18;// input m eff in kg = single clamped cantilever = m/4, double clamped string = m/2, sheet = m/4
double Q_m = 1.25e2; // Q mechanical 
double bathTemp = 1; // math temperature, kelvin

// Oscillator type specific values
//////////// String/sheet thickness to calculate g0
double thickness = 10*0.3e-9; //m
/////////// If a string to calculate g0 where string must be narrow compared to toroid minor diameter
double string_width = 1100e-9; //m

////////////////////////////////////////////////////////////////////

int main(){
	Toroid  MySuperToroid(Tor_radius,Small_radius, D_mode, f_r, coupling, Q_opt, n_toroid, n_dielectric, wavelength); // add peroperties from top
	double CC = (pow(n_resonator,2) - 1)*pow(f_r,2)*exp(-2*MySuperToroid.alpha*x0);
	
///////////////////////////////////////////////////////////////////////////////////////////////////// Select code in here to use
	
//	FOR RESONATOR WITH KNOWN g0 ////// 		EDIT 
//double g0 = Hz2Rad_FUNC(4.9e6 * 1e9); // Hz/m 
//OscillatorKnown_g0 MySuperOscillator(Omega_m, mass_ef, Q_m, g0);
//////////////////////////////////

//	FOR SHEET TO CALCULATE g0 ////// 		EDIT 
//OscillatorSheet MySuperOscillator(Omega_m, mass_ef, Q_m, MySuperToroid.sample_length_y, MySuperToroid.sample_length_x, MySuperToroid.V_cav(), MySuperToroid.alpha, thickness, Omega_cav,CC);
//////////////////////////////////

//	FOR STRING TO CALCULATE g0 WITH HORIZONTAL ALIGNMENT ////// EDIT 
OscillatorString MySuperOscillator(Omega_m, mass_ef, Q_m, MySuperToroid.sample_length_y, MySuperToroid.sample_length_x, MySuperToroid.V_cav(), MySuperToroid.alpha, thickness, Omega_cav,CC, string_width, Tor_radius);
//////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////// End of editable code
	
	double MGW = mass_ef*Omega_m*MySuperOscillator.Gamma_m(); 
	// used in calculations
		
	double OMKAP = pow(Omega_m,2)+pow(MySuperToroid.Kappa(Omega_cav)/2,2);
	// used in calculations

	double G_zpf = MySuperOscillator.g0_val()*MySuperOscillator.x_zpf();   
	// Shift with zero point fluctuation
	
	double SQL = pow(MySuperToroid.coupling,-0.5)*(hBar/MGW); 
	// minimal imprecision for optimised power
	
	double Nphoton_SQL = MGW*OMKAP/(2*hBar*MySuperToroid.Kappa(Omega_cav)*pow(MySuperOscillator.g0_val(),2)*pow(MySuperToroid.coupling,0.5)); 
	// eqtn 2.126. Order 1e5 photons. Max interaction so fewer photons
	
	double G_root_Nphoton_SQL = G_zpf*pow(Nphoton_SQL,0.5); 
	// the noise in measurement of zero point motion
	
	double Nbath = (kB*bathTemp)/(hBar*Omega_m);
	// number of phonons in the bath at
	
	double Power_SQL = hBar*Omega_cav*MySuperToroid.Kappa(Omega_cav)*Nphoton_SQL*0.25/MySuperToroid.coupling; 
	// order 0.5 micro watt
	
	double Force_rp = hBar*MySuperOscillator.g0_val()*Nphoton_SQL; 
	// order nano-newtons
	
	double Imprecision_qn = OMKAP/(4*Nphoton_SQL*pow(MySuperOscillator.g0_val(),2)*MySuperToroid.coupling*MySuperToroid.Kappa(Omega_cav)); 
	//eqtn 2.119, weaker measurement, greater imprecision
	
	double x_min = pow(Imprecision_qn,0.5); 
	//smallest possible displacement m/sqrt(Hz) eqtn 2.120
	
	/////////////////// PRINT THESE OUT
// cout << "Resonator type = " << resonator_type << " , 

cout << "For a mechanical frequency of " << Omega_m/(2*pi) << " Hz" << endl;
cout << "At temperature of " << bathTemp << " kelvin, number of phonons in the bath (nBath) is " << Nbath << endl;
cout << "x_zpt = " << MySuperOscillator.x_zpf() <<  " m" << endl;
cout << "g0 = " <<  g0_to_MHz_nm(MySuperOscillator.g0_val()/(pi*2)) << " MHz/nm" << endl;
cout << "G_zpf = " << G_zpf/(pi*2) << " Hz"<< endl;
cout << "**********************" << endl;

cout << "Gamma = " << MySuperOscillator.Gamma_m()/(pi*2) <<  " Hz phonon decay rate" << endl;
cout << "Kappa = " << MySuperToroid.Kappa(Omega_cav)/(pi*2) << " Hz OPTICAL "<< endl;
cout << "Total population rate nBath*Gamma = " << Nbath*MySuperOscillator.Gamma_m()/(pi*2) << " Hz" << endl;

cout << "G1WB = " << G_zpf/(max(MySuperOscillator.Gamma_m(), MySuperToroid.Kappa(Omega_cav)))<< " unit less, = G_zpf/max{Kappa,Gamma}" <<endl;
cout << "G2WB = " <<G_zpf/(max(Nbath*MySuperOscillator.Gamma_m(),MySuperToroid.Kappa(Omega_cav)))<< " unit less, = G_zpf/max{Kappa,nBath*Gamma}" <<endl;

cout << "G3WB = " << G_zpf/(sqrt(MySuperOscillator.Gamma_m() * MySuperToroid.Kappa(Omega_cav)))<< " unit less, = G_zpf/sqrt(Kappa*Gamma)" <<endl;
cout << "G4WB = " << G_zpf/(sqrt(MySuperOscillator.Gamma_m() * MySuperToroid.Kappa(Omega_cav) * Nbath))<< " unit less, = G_zpf/sqrt(Kappa*Gamma*Nbath)" <<endl;
cout << "**********************" << endl;

cout << "Toroid y field distance sampled " << MySuperToroid.sample_length_y*1e6 << " microns " << endl;
cout << "Field decay length 1/alpha = " << 1/MySuperToroid.alpha << " m" << endl;
cout << "G_Kap = " << G_zpf/MySuperToroid.Kappa(Omega_cav) << " unit less"<< endl;
cout << "G_Gam = " << G_zpf/MySuperOscillator.Gamma_m() << " unit less" << endl;
cout << "GG_Kap_Gam = " << pow(G_zpf,2)/(MySuperToroid.Kappa(Omega_cav)*MySuperOscillator.Gamma_m()) << "  unit less" << endl;
cout << "Nphoton_SQL = "<< Nphoton_SQL << " photons" << endl;
cout << "G_root_Nphoton_SQL = " << G_root_Nphoton_SQL << "check units" << endl;
cout << "x_min = " << x_min*(1e18) << "am/root(Hz). " << endl;
	
	if(string_width>MySuperToroid.sample_length_y)
		cout<<"!!!!!!!!! string wider than toroid y field TRY AGAIN FOR MEANINGFUL RESULTS !!!!!!!!!!!!!!!"<<endl;
	else
	
	return 0;
};