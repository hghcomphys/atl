"""
Defining molecular sections meta-class and subsequent classes

"""

# from abc import	ABCMeta, abstractmethod
from mf_base import *
from copy import deepcopy


class MolecularSection:
    """
    Defining base class for each molecular frame section such as AtomSection.
    """
    def __init__(self, name):
        self._items = []
        self._name = str(name)

    def add(self, item):
        self._items.append(item)

    def add_items(self, items):
        for item in items:
            self.add(items)

    def get_items(self):
        return self._items

    def get_items_number(self):
        return len(self._items)

    def get_name(self):
        return self._name

    def __str__(self):
        out = self._name + "\n\n"
        for item in self._items:
            out += str(item) + '\n'
        return out

    def make(self, section):
        """
        This method makes a given subclass of molecular section (i.e. AtomicSection) and return it as a new instance.
        The reason for this method is to make a specific molecular section just by simply giving its name.
        """
        try:
            molecular_section_instance = eval(str(section))()

        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected subclass name for %s!" % self.__class__.__name__)

        return molecular_section_instance


class AtomsSection(MolecularSection):
    """
    This class contains particularly list of Atom class with relevant methods for the atoms.
    """

    def __init__(self):
        MolecularSection.__init__(self, "Atoms")

    def add(self, atom):
        if isinstance(atom, Atom):
            self._items.append(atom)  # always len(items)=1 (replacing)
        else:
            raise AssertionError("Unexpected type for %s!" % self.__class__.__name__)

    def add_atoms(self, atoms):
        for atom in atoms:
            self.add(atom)
        return self

    def get_atoms(self):
        return self._items

    def get_atoms_number(self):
        return len(self._items)

    def __eq__(self, other):
        """
        This method defines equal '=' operator between two atoms section instances.
        """
        if isinstance(other, AtomsSection):
            self._name = other.get_name()
            self._items = deepcopy(other.get_atoms())
            return self
        else:
            AssertionError("Expected %s for '=' operator!" % self.__class__.__name__)

    def __add__(self, other):
        """
               This method defines '+' between atoms section instances.
        """
        if isinstance(other, AtomsSection):
            new_atom_section = AtomsSection()
            new_atom_section.add_atoms(deepcopy(self.get_atoms()))
            new_atom_section.add_atoms(deepcopy(other.get_atoms()))
            return new_atom_section
        else:
            AssertionError("Expected %s for '=' operator!" % self.__class__.__name__)


class BoxSection(MolecularSection):
    """
    This class contains simulation box info and relevant methods.
    """
    def __init__(self):
        MolecularSection.__init__(self, 'Box')
        self._items = None

    def add(self, item):
        if isinstance(item, Box):
            self._items = item  # always len(items)=1 (replacing)
        else:
            raise AssertionError("Unexpected type for %s!" % self.__class__.__name__)

    def __str__(self):
        return str(self._items)


# class BondsSection(MolecularSection):
#
#     def __init__(self):
#         MolecularSection.__init__(self, "Bonds")
#
#
# class AnglesSection(MolecularSection):
#
#     def __init__(self):
#         MolecularSection.__init__(self, "Angles")
#
#
# class DihedralsSection(MolecularSection):
#
#     def __init__(self):
#         MolecularSection.__init__(self, "Dihedrals")
#
#
# class ImpropersSection(MolecularSection):
#
#     def __init__(self):
#         MolecularSection.__init__(self, "Impropers")
#
#
# class MassesSection(MolecularSection):
#
#     def __init__(self):
#         MolecularSection.__init__(self, 'Masses')
#
#
# class MolTypeSection(MolecularSection):
#
#     def __init__(self):
#         MolecularSection.__init__(self, 'MolType')
#         self.items = None
#
#     def add(self, item):
#         if isinstance(item, MolType):
#             self.items = item  # always len(items)=1 (replacing)
#         else:
#             raise AssertionError("Unexpected type for MolTypeSection!")
#
#     def __str__(self):
#         return str(self.items)


# ==========================================================================================


if __name__ == '__main__':

    atom1 = Atom(atom_id=1, molecule_id=1, atom_type=1, q=0, x=0.3, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atom2 = Atom(atom_id=2, molecule_id=1, atom_type=1, q=0, x=0.5, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atoms_block = AtomsSection()
    atoms_block.add(atom1)
    atoms_block.add(atom2)
    print (atoms_block)

    box1 = Box(xlo=1, xhi=2, ylo=-1, yhi=2.3, zlo=92, zhi=23)
    box_block = BoxSection()
    print (box_block)

    # bond1 = Bond(bond_id=1, bond_type=1, aid_i=1, aid_j=2)
    # bond2 = Bond(bond_id=2, bond_type=1, aid_i=1, aid_j=2)
    # bonds_block = BondsSection()
    # bonds_block.add(bond1)
    # bonds_block.add(bond2)
    # print (bonds_block)
    #
    # angle1 = Angle(angle_id=1, angle_type=1, aid_i=2, aid_j=4, aid_k=5, label=' # water angle')
    # angles_block = AnglesSection()
    # angles_block.add(angle1)
    # print (angles_block)
    #
    # dihedral1 = Dihedral(dihedral_id=1, dihedral_type=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    # dihedral_block = DihedralsSection()
    # dihedral_block.add(dihedral1)
    # print (dihedral_block)
    #
    # improper1 = Improper(improper_id=1, improper_type=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    # improper_block = ImpropersSection()
    # improper_block.add(improper1)
    # print (improper_block)
    #
    # mass1 = Mass(mass_id=1, mass=2.3, label='O')
    # mass2 = Mass(mass_id=2, mass=0.33, label='H')
    # masses_block = MassesSection()
    # masses_block.add(mass1)
    # masses_block.add(mass2)
    # print (masses_block)
    #
    # moltype1 = MolType(atoms=[100, 2], bonds=[21, 1])
    # moltype_block = MolTypeSection()
    # moltype_block.add(moltype1)
    # print (moltype_block)