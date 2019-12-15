"""
Python wrapper for calling subroutine from hbond_fort.90 using f2py.
"""

def calculate_hbond(file_name, pbc_box, sel_type=['O', 'H', 'O'], 
    criteria=[3.5, 2.5, 30.0], z_confined=False, frames=[1, 1000000, 1]):

    """
    This subroutine calculates total number of hydrogen bonds, number of donor and acceptor 
    from .xyz output format via averaging over specified frames.
    """
    import os
    # making .so file (ih has to be automated)
    # os.system("f2py -c rdf_fort.f90 -m rdf_fort")
    import atl.hbond_fort # !!! (makefile needed)

    # calling Fortran subroutine
    atl.hbond_fort.calc_hbond_fort(file_name, sel_type[0], sel_type[1], 
        sel_type[2], criteria, pbc_box, z_confined, frames)