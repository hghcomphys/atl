"""
Molecular frame class
"""

# from mf_section import MolecularSection
from mf_ase import Adaptor
from mf_formatter import *
from copy import deepcopy


class MolecularFrame:

    def __init__(self, name='Molecular Frame'):
        self._molecular_sections = dict()  # setting empty dictionary for molecular sections field
        self._name = str(name)  # giving a name for molecular frame (info field)

    def __str__(self):
        """
        This method defines string conversion for molecular frame.
        """
        out = self._name + '\n'
        for mol_sec in self._molecular_sections.values():
            out += str(mol_sec) + '\n'
        return out

    def get_molecular_section(self, section_name):
        """
        This method returns the molecular sections by specifying the section name.
        """
        if section_name in self._molecular_sections.keys():
            return self._molecular_sections[section_name]
        else:
            AssertionError("Cannot find section name for %s!" % self.get_molecular_section.__name__)

    def get_molecular_sections(self):
        """
        This method returns all molecular sections in form of dictionary.
        """
        return self._molecular_sections

    def set_molecular_section(self, molecular_section):
        """
        This method sets the specified molecular section.
        """
        if isinstance(molecular_section, MolecularSection):
            self._molecular_sections[molecular_section.get_name()] = molecular_section
        else:
            AssertionError("Unexpected molecular section for %s!" % self.__class__.__name__)

    def set_molecular_sections(self, molecular_sections):
        """
        This method sets molecular sections in form of dictionary.
        """
        if isinstance(molecular_sections, dict):
            for mol_sec in molecular_sections.values():
                self.set_molecular_section(mol_sec)
        else:
            AssertionError("Expected dict input argument for %s!" % self.set_molecular_sections.__name__)

    def import_from(self, package_instance, package_name):
        """
        This method imports molecular frame from an external module such as ASE.
        """
        tmp = Adaptor(package_instance).make(package_name).get_molecular_sections()
        self.set_molecular_sections(tmp)
        return self

    def read(self, file_name, file_format='xyz'):
        """
        This method reads a file with specified format into molecular frame.
        """
        self.set_molecular_sections(Formatter(self).make(file_format.upper()).read(file_name))
        return self

    def write(self, file_name, file_format='xyz'):
        """
        This method writes molecular frame into a file with specified format.
        """
        Formatter(self).make(file_format.upper()).write(file_name)

    def get_name(self):
        return self._name

    def export_to(self):
        pass

    def __eq__(self, other):
        """
        This method defines equal '=' operator between two molecular frame instances.
        """
        if isinstance(other, MolecularFrame):
            self._name = other.get_name()
            self._molecular_sections = deepcopy(other.get_molecular_sections())
            return self
        else:
            AssertionError("Expected %s for '=' operator!" % self.__class__.__name__)

    def __add__(self, other):
        """
        This method defines '+' between molecular frame instances.
        """
        if isinstance(other, MolecularFrame):
            new_mf = MolecularFrame(self.get_name() + ' + ' + other.get_name())
            for mol_sec in ["Atoms"]: #, "Box"]:
                new_mf.set_molecular_section(self.get_molecular_section(mol_sec) + other.get_molecular_section(mol_sec))
            return new_mf
        else:
            AssertionError("Expected %s for '+' operator!" % self.__class__.__name__)





# ==========================================================================================


if __name__ == '__main__':

    from ase.build import bulk
    crys = bulk('Cu', 'fcc', a=3.6, orthorhombic=True)
    from ase.build.supercells import make_supercell
    import numpy as np
    P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * 10
    crys_supcell = make_supercell(crys, P)

    mf1 = MolecularFrame('supercell')
    mf1.import_from(crys_supcell, package_name="ASE")
    # print (mf)

    file_name = '/home/hossein/Desktop/test.xyz'
    # mf1.write(file_name)

    # mf = MolecularFrame().read(file_name)
    # print(mf)

    #mf2 = MolecularFrame()
    mf2 = mf1
    # print(mf2)

    mf3 = mf1 + mf2
    print(mf3.get_name())
    print(mf3.get_molecular_section("Atoms").get_atoms_number())
    mf3.write(file_name)
    print (mf3.get_molecular_section("Atoms"))

