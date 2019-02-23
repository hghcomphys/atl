"""
Python wrapper for calling subroutine from rdf_fort.90 using f2py.
"""

def calculate_rdf(file_name='dump.xyz', sel_type='', pbc_box=[0, 0, 0],
       nr_mesh=100, r_cutoff=10.0,
       lateral=False, delta_z=1.0,
       frames=[1, 1000000, 1]):
    """
    This subroutine calculates radial distribution function (RDF) between atoms
    (at this moment atoms with type) from .xyz output format via averaging over
    specified frames.
    """
    import os
    # making .so file (ih has to be automated)
    os.system("f2py -c rdf_fort.f90 -m rdf_fort")
    import atl.rdf_fort

    for i in range(3):
        if pbc_box[i] == 0.0:
            pbc_box[i] = 1.0E6  # setting large box size to disable pbc
            print ('disable pbc')

    start_frame, stop_frame, step_frame = frames[0], frames[1], frames[2]

    # calling Fortran subroutine
    atl.rdf_fort.calc_rdf_fort(file_name, pbc_box, nr_mesh, r_cutoff, lateral, delta_z,
                       sel_type, start_frame, stop_frame, step_frame)