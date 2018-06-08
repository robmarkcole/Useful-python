"""
Constants in inalphabetical order. Use lower case to distingush from
global variables which are upper case. Dont bother to pylint this file.

Sources
http://docs.astropy.org/en/stable/constants/index.html
https://docs.scipy.org/doc/scipy/reference/constants.html

Author R.Cole
"""
from astropy import constants as astro_const
import numpy as np
from scipy.constants import physical_constants as scy_const

absolute_zero_celcius = -273.15 # Kelvin.
boltzmann = scy_const['Boltzmann constant'][0]
electron_charge = scy_const['elementary charge'][0] # Coloumbs per electron
gravitational_constant = astro_const.G.value  # Gravitational constant, m3 / (kg s2)
earth_mass = astro_const.M_earth.value  # Earth mass. kg
earth_radius = astro_const.R_earth.value  # Earth equatorial radius, m
earth_temperature = 290 # Kelvin, from Larson
planck = scy_const['Planck constant'][0] # h
pi = np.pi
speed_of_light = scy_const['speed of light in vacuum'][0]
sun_temperature = 6000 # Kelvin, from internet
zero_celcius_in_kelvin = -1 * absolute_zero_celcius
