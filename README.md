# Atomic Tools Library
Atomic tools library (ATL) is the package for molecular simulations with Python and having core modules in C and Fortran (not implemented yet). It is planned to provide user-friendly and advanced tool set for carrying out an easier molecular simulation mainly suitable for [LAMMPS][1] package in terms of preparing input data file and performing post-processing of simulation outputs.

Currently, ATL contains some features as follows:

* __Molecular Frame__ tools for working with [LAMMPS][1] data input file (i.e. modifying molecular topologies, merging molecules)
* Water models (SPC/E, TIP5P) bond&angle info generation from *.xyz* file format
* Reading [LAMMPS][1] log file into [Pandas](https://pandas.pydata.org/) data frame
* Inter-molecular Lennard-Jones parameters generator
* Simple data analysis and visualization (i.e. smoothing data)
* Total dipole

Example:
```python
import atl # Atomic Tools Library
log = atl.read_log_pandas(filename="log.lammps", run=2)
log.plot(x='Step', y='Temp')
```

[1]:(https://lammps.sandia.gov/)
