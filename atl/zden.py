"""
Python wrapper for calling subroutine from zden_fort.90 using f2py.
"""

def calculate_zden(file_name, sel_type, zlim, nz=100, frames=[1, 1000000, 1]):
    """
    This subroutine calculates density pfrofile along z-axis 
    from .xyz output format via averaging over specified frames.
    """
    import os
    # making .so file (ih has to be automated)
    # os.system("f2py -c rdf_fort.f90 -m rdf_fort")
    import atl.zden_fort # !!! (makefile needed)

    # calling Fortran subroutine
    atl.zden_fort.calc_zden_fort(file_name, sel_type, zlim, nz, frames)