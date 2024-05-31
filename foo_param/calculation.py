from math import pi
from .utils import complex_parameterization


def calculate_volume(radius) -> object:
    """
    Calculate the volume of a sphere using the complex Foo et al. parameterization.

    Parameters:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")

    volume = complex_parameterization(radius)
    return volume
