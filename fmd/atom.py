""" Atom and AtomSection"""

from mf_section import MolecularSection
from mf_error import int_ge_zero
from copy import deepcopy


class Atom:
    """Atom class contains all info about atom and can be used in atom section as one type of molecular sections."""

    def __init__(self, atom_id, molecule_id, atom_type, q, x, y, z, imx=0, imy=0, imz=0, label=''):
        try:
            self.__atom_id = int_ge_zero(atom_id)  # atom id
            self.__molecule_id = int_ge_zero(molecule_id)  # molecule id
            self.__atom_type = int_ge_zero(atom_type)  # atom type
            self.__q = float(q)  # atom charge
            self.__x = float(x)  # x-coordinate
            self.__y = float(y)  # y-coordinate
            self.__z = float(z)  # z-coordinate
            self.__imx = int(imx)  # image index along-x
            self.__imy = int(imy)  # image index along-y
            self.__imz = int(imz)  # image index along-z
            self.__label = str(label)  # atom label (string)

        except ValueError:
            raise AssertionError("Unexpected value for initializing %s!" % self.__class__.__name__)

    @property
    def x(self):
        """returns x position of atom"""
        return self.__x

    @property
    def y(self):
        """returns y position of atom"""
        return self.__y

    @property
    def z(self):
        """returns z position of atom"""
        return self.__z

    @property
    def label(self):
        """return assigned label of atom"""
        return self.__label

    def __str__(self):
        """defines string conversion for Atom"""
        out = ''
        for attribute in [self.__atom_id, self.__molecule_id, self.__atom_type, self.__q, self.__x, self.__y, self.__z,
                          self.__imx, self.__imy, self.__imz, self.__label]:
            out += str(attribute) + ' '
        return out


class AtomsSection(MolecularSection):
    """
    This class contains particularly list of Atom intances with relevant methods for the atoms section.
    """
    def __init__(self, atoms=None):
        # TODO: AtomSection inheritades from MolecularSection class!
        MolecularSection.__init__(self, 'Atoms')
        # initialize Atom by either atom or list of atoms
        if isinstance(atoms, Atom):
            self.add(atoms)
        if isinstance(atoms, list):
            self.add_atoms(atoms)

    @property
    def atoms(self):
        """returns list of atoms"""
        return self.items

    def add(self, atom):
        if not isinstance(atom, Atom):
            raise AssertionError("Expected Atom type for %s add method!" % self.add.__name__)
        self.atoms.append(atom)
        return self

    def add_atoms(self, atoms):
        if not isinstance(atoms, list):
            raise AssertionError("Unexpected a list of atoms %s method!" % self.add_atoms.__name__)
        # adding list of atoms
        for atom in atoms:
            self.add(atom)
        return self

    def get_atoms_number(self):
        """returns number of atoms"""
        return len(self.atoms)

    def __add__(self, other):
        """ This method defines '+' between atoms section instances."""
        if not isinstance(other, AtomsSection):
            AssertionError("Expected %s for '=' operator!" % self.__class__.__name__)
        # integrate two atom sections
        # TODO: simply joining two list of atoms
        new_atom_section = AtomsSection()
        new_atom_section.add_atoms(deepcopy(self.atoms))
        new_atom_section.add_atoms(deepcopy(other.atoms))
        # returning a new atom section
        return new_atom_section


if __name__ == '__main__':

    atom1 = Atom(atom_id=1, molecule_id=1, atom_type=1, q=+0.1, x=0.3, y=0.4, z=0.7, imx=0, imy=0, imz=0, label='Cu')
    atom2 = Atom(atom_id=2, molecule_id=2, atom_type=2, q=-0.1, x=0.5, y=0.6, z=0.8, imx=1, imy=1, imz=1, label='Fe')
    print (AtomsSection([atom1, atom2]))
