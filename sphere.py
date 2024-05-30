from .core.py import foo_parameterization

def calculate_sphere_volume(radius):
    """
    Calculate the volume of a sphere using the Foo et al. parameterization.
    
    Parameters:
        radius (float): The radius of the sphere.
    
    Returns:
        float: The volume of the sphere.
    """
    return foo_parameterization(radius)