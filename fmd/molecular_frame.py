"""
Molecular frame class
"""

from mf_section import MolecularSection
from mf_ase import Adaptor
from mf_formatter import *


class MolecularFrame:

    def __init__(self):
        self.molecular_sections = dict()  # dictionary of molecular sections

    def get_molecular_section(self, section_name):
        """
        This method returns an specified molecular section from the molecular frame.
        """
        if section_name in self.molecular_sections.keys():
            return self.molecular_sections[section_name]
        else:
            AssertionError("Unexpected section name for MolecularFrame!")

    def set_molecular_section(self, molecular_section):
        """
        This method set an specified molecular section into molecular frame.
        """
        if isinstance(molecular_section, MolecularSection):
            self.molecular_sections[molecular_section.name] = molecular_section
        else:
            AssertionError("Unexpected section name for MolecularFrame!")

    def __str__(self):
        out = 'Molecular Frame'
        for key,value in self.molecular_sections.items():
            out += str(value) + '\n'
        return out

    def _import(self, package_object, package_name):
        self.molecular_sections = Adaptor(package_object).make(package_name).get_molecular_sections() # direct assignment !!!
        return self

    def _export(self):
        pass

    def read(self, file_name, file_format='xyz'):
        self.set_molecular_section = Formatter(self).make(file_format.upper()).read(file_name) # direct assignment !!!
        return self

    def write(self, file_name, file_format='xyz'):
        Formatter(self).make(file_format.upper()).write(file_name)


# ==========================================================================================


if __name__ == '__main__':

    from ase.build import bulk
    crys = bulk('Cu', 'fcc', a=3.6, orthorhombic=True)
    from ase.build.supercells import make_supercell
    import numpy as np
    P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * 10
    crys_supcell = make_supercell(crys, P)

    mf = MolecularFrame()
    mf._import(crys_supcell, package_name="ASE")

    file_name = '/home/hossein/Desktop/test.xyz'
    mf.write(file_name)
    print(MolecularFrame().read(file_name))
    #print(mf.get_molecular_section("Atoms"))

