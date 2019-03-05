"""
Molecular frame class
"""

from molframe_ase import AdaptorASE
from molframe_io import *


class MolecularFrame:

    def __init__(self):
        self.sections = dict()  # dictionary of molecular sections

    def __str__(self):
        out = 'Molecular Frame'
        for key,value in self.sections.items():
            out += str(value) + '\n'
        return out

    def import_ase(self, ase_boject):
        self.sections = AdaptorASE(ase_boject).get_molecular_frame_sections()

    def write(self, file_name, format='xyz'):
        Formatter(self).make(format.upper()).write(file_name)


# ==========================================================================================


if __name__ == '__main__':

    from ase.build import bulk
    crys = bulk('Cu', 'fcc', a=3.6, orthorhombic=True)
    from ase.build.supercells import make_supercell
    import numpy as np
    P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * 10
    crys_supcell = make_supercell(crys, P)

    mf = MolecularFrame()
    mf.import_ase(crys_supcell)
    # print(mf)
    mf.write('/home/hossein/Desktop/test.xyz')

