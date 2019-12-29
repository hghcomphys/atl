# Atomic Tools Library
Atomic tools library (ATL) is the package for molecular simulations with Python and having core modules implemented in C and Fortran. It is planned to provide user-friendly and advanced tools for carrying out an easier molecular simulation suitable for the [LAMMPS][1] package in terms of preparing input data file and performing post-processing of simulation outputs.

Currently, ATL contains some features as follows:

* __Molecular Frame__ tools for working with [LAMMPS][1] data input file (i.e. modifying molecular topologies, merging molecules)
* Generate Water models (SPC/E, TIP5P) bond and angle info from *.xyz* file format
* Read [LAMMPS][1] logfile into [Pandas](https://pandas.pydata.org/) data frame
* Basic data analysis and visualization (i.e. smoothing data)
* Total dipole from input structure files
* Radial distribution function (RDF), lateral-RDF
* Density profile
* Average number of H-bonds

Example:
```python
import atl # Atomic Tools Library
log = atl.read_log_pandas(filename="log.lammps", run=2)
log.plot(x='Step', y='Temp')
```
For more examples, see `example` folder.

[1]:(https://lammps.sandia.gov/)
