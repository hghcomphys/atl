# ATL: Atomic Tools Library
The atomic tools library (`atl`) is a Python tool aimed at facilitating molecular dynamics simulations, 
with essential computational kernels implemented in Fortran.
It is planned to provide an user-friendly tool for carrying out an easier molecular 
simulation suitable for the [LAMMPS][1] package in terms of preparing input 
and performing post-processing of the simulation outputs.

Features:

* Manipulation of [LAMMPS][1] molecule topologies, including modifications and merging of molecules.
* Generation of water models (such as SPC/E and TIP5P) and extraction of bond and angle information from `.xyz` file format.
* Reading [LAMMPS][1] logfiles into [Pandas](https://pandas.pydata.org/) data frames for easy analysis.
* Basic data analysis and visualization capabilities.
* Calculation of the total dipole from input structure files.
* Computation of radial distribution functions (RDF) and lateral RDF.
* Determination of density profiles.
* Calculation of average number of H-bonds and H-bond profiles.

## Example:
See [this](https://github.com/hghcomphys/atl/blob/develop/examples/atl_examples.ipynb) example jupyter notebooks.

[1]:(https://lammps.sandia.gov/)
