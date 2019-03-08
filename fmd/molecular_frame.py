"""
Molecular frame class
"""

from mf_section import MolecularSection
from mf_ase import Adaptor
from mf_formatter import *


class MolecularFrame:

    def __init__(self, name='Molecular Frame'):
        self._molecular_sections = dict()  # empty dictionary of molecular sections
        self._name = str(name)

    def __str__(self):
        out = self._name + '\n'
        for mol_sec in self._molecular_sections.values():
            out += str(mol_sec) + '\n'
        return out

    def get_molecular_section(self, section_name):
        """
        This method returns an specified molecular section from molecular frame.
        """
        if section_name in self._molecular_sections.keys():
            return self._molecular_sections[section_name]
        else:
            AssertionError("Cannot find section name for %s!" % self.get_molecular_section.__name__)

    def get_molecular_sections(self):
        return self._molecular_sections

    def set_molecular_section(self, molecular_section):
        """
        This method set an specified molecular section into molecular frame.
        """
        if isinstance(molecular_section, MolecularSection):
            self._molecular_sections[molecular_section.get_name()] = molecular_section
        else:
            AssertionError("Unexpected molecular section for %s!" % self.__class__.__name__)

    def set_molecular_sections(self, molecular_sections):
        """
        This method set molecular frame dictionary
        """
        if isinstance(molecular_sections, dict):
            for mol_sec in molecular_sections.values():
                self.set_molecular_section(mol_sec)
        else:
            AssertionError("Expected dict input argument for %s!" % self.set_molecular_sections.__name__)

    def import_from(self, package_instance, package_name):
        """
        This method import molecular frame from external package such as ASE.
        """
        tmp = Adaptor(package_instance).make(package_name).get_molecular_sections()
        self.set_molecular_sections(tmp)
        return self

    def export_to(self):
        pass

    def read(self, file_name, file_format='xyz'):
        self.set_molecular_sections(Formatter(self).make(file_format.upper()).read(file_name))
        return self

    def write(self, file_name, file_format='xyz'):
        Formatter(self).make(file_format.upper()).write(file_name)


# ==========================================================================================


if __name__ == '__main__':

    # from ase.build import bulk
    # crys = bulk('Cu', 'fcc', a=3.6, orthorhombic=True)
    # from ase.build.supercells import make_supercell
    # import numpy as np
    # P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * 10
    # crys_supcell = make_supercell(crys, P)
    #
    # mf = MolecularFrame()
    # mf.import_from(crys_supcell, package_name="ASE")
    # # print (mf)
    #
    file_name = '/home/hossein/Desktop/test.xyz'
    # mf.write(file_name)

    print(MolecularFrame().read(file_name))
    #print(mf.get_molecular_section("Atoms"))

