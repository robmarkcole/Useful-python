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

The format of the Return section is 'type : unit'. All units SI.

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

bandwidth_operating
    double : Meters
    The sensor operating bandwith, delta lambda.

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

decibels
    double : Decibels
    Decibels (dB).

dark_current
    double : Amps
    A dark current in Amps.

earth_mean_orbital_speed
    double : Meters per second
    The speed of a satellite orbiting at altitude.

earth_orbital_period
    double : Seconds
    The orbital period of a body in a circular
    orbit of the Earth

electron_full_well
    int : RMS Electrons
    The number of electrons at full well capacity.

electron_read_noise
    int : RMS Electrons
    The number of electrons constituting read noise, Nr.

electrons
    int : no units, number of electrons
    A number of electrons.

energy
    double : Joules (Watts per second)
    The energy of interest for a calculation.

exposure_time_min
    double : Seconds
    The minimum possible exposture time (sometimes referred to as
    integration time).

f_number
    double : no units
    The f-number of an optical system,F#.

focal_length
    double : Meters
    The focal length of the camera, f.

frame_rate
    double : inverse Seconds (i.e. Hz)
    The rate at which the frame (all pixels) is read.

gsd_cross
    double : Meters
    The ground sample distance at Nadir across track.

ifov
    double : Degrees
    The instantaneous field of view (IFOV) is the solid angle that a
    single pixel is sensitive to, in deg.

radiance_reference
    double : Watts per Meter squared per Sterradian per unit bandwith,
             typicaly microns in which case units (W/m^2/sr/um)
    The radiance for a reference bandwidth.

radiance_integrated
    double : Watts per Meter squared per Sterradian (W/m^2/sr)
    The radiance integrated over operating bandwidth (L_int).

integration_time
    double : Seconds
    The time of integration.

operating_temperature_min
    double : Kelvin
    The minium operating temperature for a camera.

optical_transmission_factor
    double : range 0 to 1, no units.
    The cameras optics transmission factor, typically 0.75.

photons
    int : no units
    A number of photons.

pixel_pitch
    double : Meters
    The pitch of adjacent pixels, assumed equal along and cross track.

pixels_along
    int : no units
    The number of pixels along track, Za.

pixel_dim_along
    double : Meters
    The size of a pixel along track, often identical to pixel_pitch,
    e.g. 20 microns.

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

radiated_power_nadir
    double : Watts per Steradian
    The radiated power, L, from a ground pixel at nadir.

read_out_noise_electrons
    int : no units, a number of electrons
    The read-out noise electrons, typically 25 electrons.

sensor_dim_along
    double : Meters
    The physical dimension of the camera sensor (pixel array) in the
    along track direction.

sensor_incident_power
    double : Watts
    The optical power, Pd, incident on a sensor.

shott_noise
    int : no units, assume particles
    The Shott noise sqrt(particles)

swath_at_nadir_cross
    double : Meters
    The cross track swath for a single camera.

total_noise_electrons
    int : no units, numer of electrons
    The total noise due to Shott and read-out noise.

velocity_ground_track
    double : meters per second.
    The apparent velocity, Vg, of the satellite on the ground (Earth).

wavelength
    double : Meters
    The wavelength of interest for a calculation.

wavelength_min
    double : Meters
    The minimum wavelength of response from the sensor.

weight
    double : Kilograms
    The mass of the camera.
"""

from optics_tools import const as const
import numpy as np

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

def calc_data_rate(bands_spectral,
                   bits,
                   cameras,
                   frame_rate,
                   pixels_total):
    """
    Calculate the data rate generated by an imager that may comprise multiple
    cameras.

    Returns
    -------
    double : bits per second
    """

    return bands_spectral * bits * cameras * frame_rate * pixels_total

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

def calc_energy_per_integration(sensor_incident_power,
                                integration_time):
    """
    Calculate the energy imparted to a sensor during an integration time.

    Returns
    -------
    double : Joules
    """

    return sensor_incident_power * integration_time

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

def calc_gsd_cross(altitude,
                   focal_length,
                   pixel_dim_cross):
    """
    ground sample distance (gsd) is the distance between pixel centers measured
    on the ground.
    https://en.wikipedia.org/wiki/Ground_sample_distance

    Returns
    -------
    double : meters per pixel
    """

    magnification = altitude / focal_length
    return magnification * pixel_dim_cross

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
    Calculate the pixel solid angle. gsd assumed equal along and cross track.

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
    Calculate the power radiated from a ground pixel at Nadir.

    Returns
    -------
    double : Watts per Sterradian.
    """

    return radiance_integrated * pixel_resolution_along * pixel_resolution_cross

def calc_sensor_incident_power(camera_input_power,
                               optical_transmission_factor):
    """
    Calculate the optical power incident on the sensor.

    Returns
    -------
    double : Watts
    """

    return camera_input_power * optical_transmission_factor

def calc_shott_noise(particles):
    """
    Calculate the Shott noise on a number of particles (photon or electrons).

    Returns
    -------
    int : no units, assume particles
    """

    return int(np.sqrt(particles))

def calc_swath_at_nadir_cross(gsd_cross,
                              pixels_cross):
    """
    Calculate the swath at nadir cross track.
    https://en.wikipedia.org/wiki/Swathe

    Returns
    -------
    double : meters
    """

    return gsd_cross * pixels_cross

def calc_total_noise_electrons(shott_noise_electrons,
                               read_out_noise_electrons,
                               dark_current_electrons):
    """
    Calculate the total noise electrons.

    Returns
    -------
    int : no units, assume particles
    """

    return int(np.sqrt(
        (shott_noise_electrons**2) + \
        (read_out_noise_electrons**2) + \
        (dark_current_electrons**2)
        ))

def calc_velocity_ground_track(earth_orbital_period):
    """
    Calculate the ground track velocity of an orbiting satellite.

    Returns
    -------
    double : meters per second
    """

    return 2 * const.pi * (const.earth_radius /earth_orbital_period)

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
