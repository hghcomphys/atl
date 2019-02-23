# Atomic Tools Library
# Hossein Ghorbanfekr [hgh.comphys@gmail.com]
# ---------------------------------------

from .read_data import *
from .read_xyz import *
from .write_xyz import *
from .molecular_frame import *
from .lammps_input import *
from .read_log import *
from .intermol_lj_param import *
from .smooth_data import *
from .dipole import *
from .rdf import *


# atm = atom()
# atm.aid   = aid # atom id (integer)
# atm.mid   = mid # molecule id (integer)
# atm.t     = 0 # atom type (integer)
# atm.q     = 0.0 # atom charge (real)
# atm.x     = d[1] # z position (real)
# atm.y     = d[2] # y position (real)
# atm.z     = d[3] # z position (real)
# atm.imx   = 0 # image index x (integer)
# atm.imy   = 0 # image index y (integer)
# atm.imz   = 0 # image index z (integer)
# atm.label = 0 # atom label (string)