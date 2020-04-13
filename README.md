# Atomic Tools Library
Atomic tools library (`atl`) is a python package for molecular simulations 
and having core modules implemented in Fortran. 
It is planned to provide user-friendly and advanced tools for carrying out an easier molecular 
simulation suitable for the [LAMMPS][1] package in terms of preparing input data 
file and performing post-processing of simulation outputs.

Currently, `atl` package contains some features as follows:

* molecular Frame tools for working with [LAMMPS][1] data input file such as modifying molecule topologies, merging molecules, etc.
* generate water models (SPC/E, TIP5P) bond and angle info from *.xyz* file format
* read [LAMMPS][1] logfile into [Pandas](https://pandas.pydata.org/) data frame
* basic data analysis and visualization
* total dipole from input structure files
* radial distribution function (RDF), lateral-RDF
* density profile
* average number of H-bonds, H-bond profile

## Install:
add atl path to pythonpyath using
```buildoutcfg
export PYTHONPATH=$PYTHONPATH:'/path/to/atl/root/directory'
```

## Examples:
A jupyter notebook is available in the `examples` directory.

[1]:(https://lammps.sandia.gov/)
