"""
Molecular frame class
"""

from molframe_ase import Adaptor
from molframe_io import *


class MolecularFrame:

    def __init__(self):
        self.sections = dict()  # dictionary of molecular sections

    def __str__(self):
        out = 'Molecular Frame'
        for key,value in self.sections.items():
            out += str(value) + '\n'
        return out

    def import_from(self, package_object, package_name):
        self.sections = Adaptor(package_object).make(package_name).get_molecular_frame_sections()

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
    mf.import_from(crys_supcell, package_name="ASE")
    # print(mf)
    mf.write('/home/hossein/Desktop/test.xyz', format="xyz")

