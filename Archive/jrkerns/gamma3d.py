import copy

import numpy as np
import scipy.ndimage.filters as spf
from pylinac.core.image import ArrayImage


def gamma3d(reference_image, comparison_image, doseTA=1, distTA=1, threshold=0.1):
    """Calculate the 3D gamma between the reference image and a comparison image.

    The gamma calculation is based on `Bakai et al
    <http://iopscience.iop.org/0031-9155/48/21/006/>`_ eq.6,
    which is a quicker alternative to the standard Low gamma equation.

    Parameters
    ----------
    reference_image : 3D numpy array
    comparison_image : 3D numpy array
        The size of the arrays must also be the same.
    doseTA : int, float
        Dose-to-agreement in percent; e.g. 2 is 2%.
    distTA : int, float
        Distance-to-agreement in mm.
    threshold : float
        The dose threshold percentage of the maximum dose, below which is not analyzed.
        Must be between 0 and 1.

    Returns
    -------
    gamma_map : numpy.ndarray
        The calculated gamma map.

    See Also
    --------
    :func:`~pylinac.core.image.equate_images`
    """
    ref_img = copy.copy(reference_image)
    comp_img = copy.copy(comparison_image)
    # invalidate dose values below threshold so gamma doesn't calculate over it
    ref_img.array[ref_img < threshold*np.max(ref_img)] = np.NaN

    # convert distance value from mm to pixels
    distTA_pixels = ref_image.dpmm*distTA

    # construct image gradient using sobel filter
    img_x = spf.sobel(ref_img.as_type(np.float32), 1)
    img_y = spf.sobel(ref_img.as_type(np.float32), 0)
    img_z = spf.sobel(ref_img.as_type(np.float32), 2)
    grad_img = np.sqrt(img_x**2 + img_y**2 + img_z**2)

    # equation: (measurement - reference) / sqrt ( doseTA^2 + distTA^2 * image_gradient^2 )
    subtracted_img = np.abs(comp_img-ref_img)
    denominator = np.sqrt((doseTA/100.0**2)+((distTA_pixels**2)*(grad_img**2)))
    gamma_map = subtracted_img/denominator

    return gamma_map


test_array = np.zeros((5, 5, 5))
test_array[2, 2, 2] = 5
test_img = ArrayImage(test_array, dpi=1)

ref_array = np.zeros((5, 5, 5))
ref_array[2, 2, 2] = 1
ref_image = ArrayImage(ref_array, dpi=1)

gamma_map = gamma3d(ref_image, test_img, threshold=0)

# max gamma value
print(np.max(gamma_map))
print(np.mean(gamma_map))

