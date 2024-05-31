from math import pi

def complex_parameterization(radius):
    """
    Apply the complex Foo et al. parameterization to calculate the volume.

    Parameters:
        radius (float): The radius of the sphere.

    Returns:
        float: The calculated volume.
    """
    volume = (4/3) * pi * (radius ** 3)
    return volume
