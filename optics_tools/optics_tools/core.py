"""
Author: R. Cole

Functions for calculating various properties and doing conversions.

Imager refers to the camera or cameras (where there are
multiple) on a satellite. Each camera has a sensor which comprises of an array
of pixels. Along track is the direction of travel of the satellite.

When calculating properties the name of a function is the property it returns
with calc_ prepended. Conversions are prepended with conv_ and should be named in the format
conv_input_to_output.

Equations taken from 'Space Missions Analysis and Design' 3rd Edition
by W.J.Larson. Equations are on pages 287 - 290. Symbols used by Larson are
given after the variables description, e.g. f for focal length.

Where a property has _min and _max suffixes, it is only necessary to add the
_min version to the variables list below.

Along and cross track properties are indicated by _along and _cross suffixes
respectively. It is only necessary to add either the the _along OR _cross
version to the variables list below.

The format of the Return section is 'type : unit'. All units SI. It is preferable
to calculate realistically measureable values, such as a current in Amps, rather
than a number of electrons. Also large numbers are preferable to small (0 >>) as
rounding will often turn small values to zero.

All constants to be imported from optics_tools.const.

Adhere to pep8 (run > pylint file.py) but allow lines longer than 80 chars in
order to maintain readability.

Properties (alphabetical order)
----------

altitude
    double : Meters
    The orbital altitude, h, of orbit above the Earths surface.

aperture_diameter
    double : Meters
    The diameter, D, of the entrance pupil.

bands_spectral
    int : no units
    The number of spectral bands, e.g. R/G/B/NIR = 4 bands.

bandwidth
    double : Hertz
    A bandwidth in Hertz, typically of a measurement.

bits
    int : units bits
    The bit depth, B, to encode each pixel.

blackbody_radiance
    double : Watts per Meter squared per Sterradian at a wavelength
    The spectral irradiance (Blackbody emission, temperature and wavelength
    dependent) divided by the total solid-angle of a body (4 Pi)
    gives the blackbody spectral radiance (L_lambda).

cameras
    int : no units
    The number of cameras that comprise the imager.

camera_input_power
    double : Watts
    The input power (P_in) on the camera aperture.

current
    double : Amps
    A current in Amps.

dark_current
    double : Amps per pixel
    The current arising from thermal excitation in a pixel.

dark_signal
    double : Electrons per pixel per second
    The signal arising from thermal excitation in a pixel.

decibels
    double : Decibels
    Decibels (dB).

detectivity
    double : Centimeters per sqrt Hertz per Watt (Jones units).
    The detectivity or specific detectivity of a sensor (Larson equation 9-15,
    see https://en.wikipedia.org/wiki/Specific_detectivity) is a measure of
    performance, inversely proportional to the noise equivalent power (NEP) but
    normalised for the sensors area and the integration time. Useful for
    comparing sensors of different area.

detector_bias
    double : Watts per Meter squared per Sterradian (W/m^2/sr)
    The detector bias.

detector_gain
    double : Watts per Meter squared per Sterradian (W/m^2/sr)
    The detector gain.

detector_mtf
    double: No units, range 0 - 1
    The MTF of the detector. https://spie.org/publications/tt52_21_detector_footprint_mtf?SSO=1

diffusion_factor
    double: No units, range 0 - 1
    Relates a pixel diffusion length to pixel size, where length=diffusion_factor*pixel_dim.

digital_number
    double : No units
    The number reported by a sensor for a pixel, DN.

dynamic_range
    double : No units
    The dynamic range of a detector.

earth_mean_orbital_speed
    double : Meters per second
    The speed of a satellite orbiting at altitude.

earth_orbital_period
    double : Seconds
    The orbital period of a body in a circular
    orbit of the Earth

electrons
    int : no units, number of electrons
    A number of electrons.

energy
    double : Joules (Watts per second)
    The energy of interest for a calculation.

f_number
    double : no units
    The f-number of an optical system,F#.

focal_length
    double : Meters
    The focal length of the camera, f.

frame_rate
    double : Hertz
    The rate at which the frame (all pixels) is read.

full_well_capacity
    integer : A number of electrons
    The numnber of electrons an individual pixel can hold before saturating.

gsd_cross
    double : Meters
    The ground sample distance at Nadir across track.

ifov
    double : Degrees
    The instantaneous field of view (IFOV) is the solid angle that a
    single pixel is sensitive to, in deg.

integration_time
    double : Seconds
    The time of integration.

line_rate
    double : Hertz
    The maximum rate that a line of pixels can be read.

noise_equivalent_power
    double : Watts.
    The NEP is a measure of the sensitivity of a photodetector sensor, and is
    the power (Watts) that would produce an SNR = 1.

operating_temperature
    double : Kelvin
    The minium operating temperature for a camera.

optical_transmission
    double : range 0 to 1, no units.
    The cameras optics transmission factor, typically 0.75.

photons
    int : no units
    A number of photons.

pixel_pitch_along
    double : Meters
    The pitch of adjacent pixels along track.

pixels_along
    int : no units
    The number of pixels along track, Za.

pixel_dim_along
    double : Meters
    The size of a pixel along track, often identical to pixel_pitch,
    e.g. 20 microns.

pixel_incident_power
    double : Watts
    The power incident on a pixel.

pixel_read_rate
    double : Hertz
    The rate at which a single pixel can be read, calculated from the line or
    frame rate.

pixel_solid_angle
    double : Steradians
    The pixel sold angle, can be calculate using various geometric relations.

pixel_resolution_along
    double : Meters
    The along track ground resolution at Nadir, e.g. 20  meters.

pixels_total
    int : no units
    The total number of pixels across track, Z = Zc*Za.

power_consumption
    double : Watts
    The power requirement to operate the camera.

power_supply_v
    double : Volts
    The DC power supply requirement.

quantum_efficiency
    double : no units, values in interval [0 - 1]
    The sensor quantum efficiency, QE.

radiance_spectral
    double : Watts per Meter squared per Sterradian per unit bandwith,
             typicaly microns in which case units (W/m^2/sr/um)
    The spectral radiance for a reference bandwidth.

radiance_integrated
    double : Watts per Meter squared per Sterradian (W/m^2/sr)
    The radiance integrated over operating bandwidth (L_int).

radiated_power_nadir
    double : Watts per Steradian
    The radiated power, L, from a ground pixel at nadir, equal to L_int * X * Y.

readout_noise
    integer : no units, a number of electrons
    The readout noise electrons per pixel, e.g. 25 electrons.

readout_time
    double : Seconds
    The readout time of a sensor, typically ms.

sensor_dim_along
    double : Meters
    The physical dimension of the camera sensor (pixel array) in the along track direction.

sensor_nyquist_frequency
    double : Cycles per meter
    The sensor nquist sampling spatial frequency derived from the pixel pitch.

shott_noise
    int : no units, assume particles
    The Shott noise sqrt(particles)

signal_electrons
    int : no units, number of electrons
    A number of electrons constituting a signal.

spatial_frequency
    double : Cycles per meter
    A measure of how ofter the sinusodial components of an image repeat per unit distace.

swath_at_nadir_cross
    double : Meters
    The cross track swath for a single camera.

time_delay_integrations
    int : no units
    The number of TDI integrations to perform.

velocity_ground_track
    double : meters per second.
    The apparent velocity, Vg, of the satellite on the ground (Earth).

wavelength
    double : Meters
    The wavelength of interest for a calculation.

weight
    double : Kilograms
    The mass of the camera.
"""

from optics_tools import const as const
import numpy as np

def calc_aperture_diameter(f_number, focal_length):
    """Calculate the aperture_diameter required for an f_number/focal_length."""
    return focal_length / f_number

def calc_beam_divergence(D1 : float, D2 : float, distance : float) -> float:
    """
    Calc the divergence angle from measured beamwidths.
    https://en.wikipedia.org/wiki/Beam_divergence
    
    D1 = beam diameter at position 1
    D2 = beam diameter at position 2
    distance = distance between position 1 & 2
    
    Returns
    divergence : radians
    """
    from math import atan
    x = (max(D1, D2) - min(D1, D2))/(2*distance)
    divergence = 2*atan(x)
    return divergence

def calc_blackbody_radiance(wavelength,
                            temperature):
    """
    Calculate the blackbody spectral radiance. Note this is normalised over
    4 pi.
    https://en.wikipedia.org/wiki/Planck%27s_law

    Returns
    -------
    double : Watts per Meter squared per Sterradian at a wavelength
    """

    intensity_factor = (const.planck * const.speed_of_light**2) \
                        / (2 * wavelength**5)
    power_factor = (const.planck * const.speed_of_light) \
                    / (const.boltzmann * temperature * wavelength)
    return intensity_factor / (np.exp(power_factor) - 1.0)

def calc_camera_input_power(altitude,
                            aperture_diameter,
                            radiated_power_nadir):
    """
    Calculate the input power (P_in) at the camera.

    Returns
    -------
    double : Watts
    """

    return (radiated_power_nadir / (altitude **2)) * const.pi * (aperture_diameter / 2)**2

def calc_dark_current_scaling(delta_celcius):
    """
    As a rule of thumb, dark current doubles with
    every 7 degrees celcius increase in temperature.
    This function takes a delta celcius and calculates
    the factor to multiply a dark current by.
    """
    return 2**(delta_celcius / 7)

def calc_data_rate(bands_spectral,
                   bits,
                   cameras,
                   frame_rate,
                   pixels_total,
                   time_delay_integrations):
    """
    Calculate the data rate generated by an imager that may comprise multiple
    cameras.

    Returns
    -------
    double : bits per second
    """

    return bands_spectral * bits * cameras * frame_rate * pixels_total * time_delay_integrations

def calc_detectivity(sensor_dim_along,
                     sensor_dim_cross,
                     measurement_bandwidth,
                     noise_equivalent_power):
    """
    Calculate detector detectivity D*.
    https://en.wikipedia.org/wiki/Specific_detectivity
    """
    root_area_cm = (sensor_dim_along * sensor_dim_cross * (100)**2)**0.5 # convert to sqrt(cm).
    return root_area_cm * (measurement_bandwidth**0.5) / noise_equivalent_power

def calc_detector_mtf(pixel_dim, diffusion_factor, spatial_frequency):
    '''Calculate detector MTF given a pixel dimension and diffusion factor.'''
    au = pixel_dim * spatial_frequency
    df = diffusion_factor
    left = (1/(1+2*df))*(1/(1+(2*np.pi*au*df)))
    right =  np.absolute(np.sinc(au) + 2*df*np.cos(np.pi*au))
    return left*right

def calc_diffraction_limited_beam_divergence(wavelength : float, beam_waist : float) -> float:
    """
    Diffraction limits the minimum laser beam divergence.
    Note that the beam waist is defined at the point the irradiance decreases to 
    1/e^2
    https://en.wikipedia.org/wiki/Beam_divergence
    
    wavelength : the optical wavelength in m
    beam_waist : the radius of the beam at its narrowest point
    
    Returns
    
    diff_limited_divergence : radians, the diffraction limited radial 
                              beam divergence, half cone 
    """
    from math import pi
    diff_limited_divergence = wavelength/(pi * beam_waist)
    return diff_limited_divergence

def calc_dynamic_range(full_well_capacity, readout_noise):
    """Calculate detector dynamic range."""
    return full_well_capacity / readout_noise

def calc_earth_mean_orbital_speed(altitude):
    """
    Calculate the orbital speed (m/s) of a body
    orbiting the Earth in a circular orbit in the equatorial plane
    https://en.wikipedia.org/wiki/Orbital_speed

    Returns
    -------
    double : meters per second
    """

    return np.sqrt((const.gravitational_constant * const.earth_mass)/
                   (altitude + const.earth_radius))

def calc_earth_orbital_period(altitude):
    """
    Calculate the orbital period (in seconds) of a body
    orbiting the Earth
    https://en.wikipedia.org/wiki/Orbital_period

    Returns
    -------
    double : seconds
    """

    return 2 * const.pi * np.sqrt(
        (altitude + const.earth_radius)**3 /
        (const.gravitational_constant * const.earth_mass)
        )

def calc_electrons_from_photons(photons,
                                quantum_efficiency):
    """
    Calculate the number of electrons generated by incident photons.

    Returns
    -------
    int : no units, a number of electrons
    """

    return int(photons * quantum_efficiency)

def calc_energy_per_integration(pixel_incident_power,
                                integration_time):
    """
    Calculate the energy imparted to a pixel during an integration time.

    Returns
    -------
    double : Joules
    """

    return pixel_incident_power * integration_time

def calc_f_number(aperture_diameter,
                  focal_length):
    """
    Calculate the f-number N (or f#) of an optical system.
    https://en.wikipedia.org/wiki/F-number

    Returns
    -------
    double : no units
    """

    return focal_length / aperture_diameter

def calc_focal_length(altitude, pixel_pitch, gsd):
    """Calculate the focal_length to achive a required GSD."""
    return  altitude * pixel_pitch / gsd

def calc_gsd(altitude,
             focal_length,
             pixel_dim):
    """
    ground sample distance (gsd) is the distance between pixel centers measured
    on the ground.
    https://en.wikipedia.org/wiki/Ground_sample_distance

    Returns
    -------
    double : meters per pixel
    """

    return (altitude * pixel_dim) / focal_length

def calc_ifov(pixel_dim_cross,
              focal_length):
    """
    Calculate the instantaneous field of view cross track. Note that there are
    several approaches possible.
    https://en.wikipedia.org/wiki/Field_of_view

    Returns
    -------
    double : degrees (deg)
    """

    return np.rad2deg(pixel_dim_cross / focal_length)

def calc_measurement_bandwidth(integration_time):
    """
    Calculate the bandwidth (Hertz) of a measurement.
    https://en.wikipedia.org/wiki/Specific_detectivity

    Returns
    -------
    double : Hertz.
    """

    return 1 / (2 * integration_time)

def calc_noise_equivalent_power(camera_input_power, snr):
    """Calculate the NEP."""
    return camera_input_power / snr

def calc_photons_from_energy(energy,
                             wavelength):
    """
    Calculate the number of photons equivalent to an energy.

    Returns
    -------
    int : no units
    """

    return int((energy * wavelength) / (const.planck * const.speed_of_light))

def calc_pixel_solid_angle(gsd,
                           altitude):
    """
    Calculate the pixel solid angle. gsd assumed equal along and cross track, i.e. square pixel.

    Returns
    -------
    double : Steradians
    """

    return (gsd / altitude)**2

def calc_pixel_resolution(ifov,
                          altitude):
    """
    Calculate the on-ground resolution of a pixel.

    Returns
    -------
    double : meters
    """

    return np.deg2rad(ifov) * altitude

def calc_radiated_power_nadir(radiance_integrated,
                              pixel_resolution_along,
                              pixel_resolution_cross):
    """
    Calculate the power radiated from a ground pixel at Nadir, equals Lint * X  *Y.

    Returns
    -------
    double : Watts per Sterradian.
    """

    return radiance_integrated * pixel_resolution_along * pixel_resolution_cross

def calc_pixel_incident_power(camera_input_power,
                              optical_transmission):
    """
    Calculate the optical power incident on a pixel.

    Returns
    -------
    double : Watts
    """

    return camera_input_power * optical_transmission

def calc_sensor_nyquist_frequency(pixel_pitch):
    """
    Calculate the nyquist sampling frequency of a sensor.

    Returns
    -------
    double : Cycles per meter
    """

    return 1/(2 * pixel_pitch)

def calc_shott_noise(particles):
    """
    Calculate the Shott noise on a number of particles (photon or electrons).

    Returns
    -------
    int : no units, assume particles
    """

    return int(np.sqrt(particles))

def calc_signal_photons(altitude,
                        aperture_diameter,
                        gsd,
                        integration_time,
                        optical_transmission,
                        radiance_integrated,
                        wavelength):
    """
    Calculate the number of signal photons incident on a sensor.
    """
    radiated_power = calc_radiated_power_nadir(radiance_integrated, gsd, gsd)
    camera_input_power = calc_camera_input_power(altitude, aperture_diameter, radiated_power)
    pixel_incident_power = calc_pixel_incident_power(camera_input_power, optical_transmission)
    energy_imparted = calc_energy_per_integration(pixel_incident_power, integration_time)
    photons_from_energy = calc_photons_from_energy(energy_imparted, wavelength)
    return int(photons_from_energy)


def calc_snr(altitude,
             dark_current,
             f_number,
             focal_length,
             integration_time,
             optical_transmission,
             pixel_dim,
             quantum_efficiency,
             radiance_integrated,
             readout_noise,
             wavelength):
    """Wrapper to calculate system SNR."""
    gsd = calc_gsd(altitude, focal_length, pixel_dim)
    aperture_diameter = calc_aperture_diameter(f_number, focal_length)
    signal_photons = calc_signal_photons(altitude, aperture_diameter, gsd, integration_time, optical_transmission, radiance_integrated, wavelength)
    signal_electrons = signal_photons * quantum_efficiency
    signal_electrons_shott = calc_shott_noise(signal_electrons)
    dark_electrons = conv_current_to_electrons_second(dark_current * integration_time)
    dark_electrons_shott = calc_shott_noise(dark_electrons)
    total_noise = calc_uncorrellated_noise(signal_electrons_shott, dark_electrons_shott, readout_noise)
    snr = signal_electrons / total_noise
    return snr

def calc_swath_at_nadir(gsd,
                        pixels):
    """
    Calculate the swath at nadir along or cross track.
    https://en.wikipedia.org/wiki/Swathe

    Returns
    -------
    double : meters
    """

    return gsd * pixels

def calc_uncorrellated_noise(*args):
    """
    Given a series of uncorrelated noise sources, calculat the total noise.

    Returns
    -------
    double : units of inputs, assume particles
    """

    return sum([arg**2 for arg in args])**0.5

def calc_velocity_ground_track(earth_orbital_period):
    """
    Calculate the ground track velocity of an orbiting satellite.

    Returns
    -------
    double : meters per second
    """

    return 2 * const.pi * (const.earth_radius /earth_orbital_period)

def conv_arcsec_to_radians(arcseconds : float) -> float:
    """
    Convert arcseconds to radians.
    
    arcseconds : the arcseconds to convert
    
    Returns
    radians : the input arcseconds converted to radians
    """
    from math import pi
    return arcseconds * pi/(180 * 3600)

def conv_celcius_to_kelvin(celcius):
    """
    Convert Celcius to Kelvin

    Returns
    -------
    double : Kelvin
    """

    return celcius + const.zero_celcius_in_kelvin

def conv_current_to_electrons_second(current):
    """
    Convert a current in Amps to a number of
    electrons per second.
    """
    return int(current / const.electron_charge)

def conv_decibels_to_power_ratio(decibels):
    """
    Calculate the power ratio P2/P1 where P1 = 1.

    Returns
    -------
    double : no units
    """

    return 10 ** (decibels / 10)

def conv_electrons_second_to_current(electrons):
    """
    Convert a number of electrons per second to a current in Amps.
    """
    return electrons * const.electron_charge

def conv_kelvin_to_celcius(kelvin):
    """
    Convert Kelvin to Celcius

    Returns
    -------
    double : Celcius
    """

    return kelvin - const.zero_celcius_in_kelvin

def conv_radians_to_arcsec(radians : float) -> float:
    """
    Convert radians to arcseconds.
    
    radians : the radians to convert
    
    Returns
    arcseconds : the input radians converted to arcseconds
    """
    from math import pi
    return radians * (180 * 3600)/pi
