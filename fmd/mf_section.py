"""
Defining molecular sections meta-class and subsequent classes

"""

# from abc import	ABCMeta, abstractmethod
from mf_base import *


class MolecularSection:
    """
    Defining base class for each molecular frame section.
    """
    def __init__(self, name):
        self.items = []
        self.name = name

    def add(self, item):
        self.items.append(item)

    def add_list(self, items):
        for item in items:
            self.items.append(item)

    def get_list(self):
        return self.items

    def get_len(self):
        return len(self.items)

    def __str__(self):
        out = self.name + "\n\n"
        for item in self.items:
            out += str(item) + '\n'
        return out

    # static method, this is implicitly a class method
    def make(section):
        try:
            block_object = eval(str(section))()

        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected type for MolFrameBlock!")
        return block_object


class AtomsSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, "Atoms")

    def get_atoms(self):
        return self.items

    def get_atoms_number(self):
        return len(self.items)


class BondsSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, "Bonds")


class AnglesSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, "Angles")


class DihedralsSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, "Dihedrals")


class ImpropersSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, "Impropers")


class MassesSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, 'Masses')


class BoxSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, 'Box')
        self.items = None

    def add(self, item):
        if isinstance(item, Box):
            self.sections = item  # always len(items)=1 (replacing)
        else:
            raise AssertionError("Unexpected type for BoxSection!")

    def __str__(self):
        return str(self.sections)


class MolTypeSection(MolecularSection):

    def __init__(self):
        MolecularSection.__init__(self, 'MolType')
        self.items = None

    def add(self, item):
        if isinstance(item, MolType):
            self.sections = item  # always len(items)=1 (replacing)
        else:
            raise AssertionError("Unexpected type for MolTypeSection!")

    def __str__(self):
        return str(self.sections)


# ==========================================================================================


if __name__ == '__main__':

    atom1 = Atom(atom_id=1, molecule_id=1, atom_type=1, q=0, x=0.3, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atom2 = Atom(atom_id=2, molecule_id=1, atom_type=1, q=0, x=0.5, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atoms_block = AtomsSection()
    atoms_block.add(atom1)
    atoms_block.add(atom2)
    print (atoms_block)

    bond1 = Bond(bond_id=1, bond_type=1, aid_i=1, aid_j=2)
    bond2 = Bond(bond_id=2, bond_type=1, aid_i=1, aid_j=2)
    bonds_block = BondsSection()
    bonds_block.add(bond1)
    bonds_block.add(bond2)
    print (bonds_block)

    angle1 = Angle(angle_id=1, angle_type=1, aid_i=2, aid_j=4, aid_k=5, label=' # water angle')
    angles_block = AnglesSection()
    angles_block.add(angle1)
    print (angles_block)

    dihedral1 = Dihedral(dihedral_id=1, dihedral_type=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    dihedral_block = DihedralsSection()
    dihedral_block.add(dihedral1)
    print (dihedral_block)

    improper1 = Improper(improper_id=1, improper_type=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    improper_block = ImpropersSection()
    improper_block.add(improper1)
    print (improper_block)

    box1 = Box(xlo=1, xhi=2, ylo=-1, yhi=2.3, zlo=92, zhi=23)
    box_block = BoxSection()
    print (box_block)

    mass1 = Mass(mass_id=1, mass=2.3, label='O')
    mass2 = Mass(mass_id=2, mass=0.33, label='H')
    masses_block = MassesSection()
    masses_block.add(mass1)
    masses_block.add(mass2)
    print (masses_block)

    moltype1 = MolType(atoms=[100, 2], bonds=[21, 1])
    moltype_block = MolTypeSection()
    moltype_block.add(moltype1)
    print (moltype_block)