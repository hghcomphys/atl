"""Defining molecular sections"""

from copy import deepcopy


class MolecularSection:
    """Defining base class for each molecular frame section such as AtomSection."""
    def __init__(self, name):
        self.__name = str(name)  # setting molecular section name
        self.__items = []  # empty list of items

    @property
    def name(self):
        """This method returns given name of molecular section."""
        return self.__name

    @property
    def items(self):
        """This method returns list of items within molecular section."""
        return self.__items

    def add(self, item):
        """This method adds an item to molecular section."""
        self.__items.append(item)
        return self

    def add_items(self, items):
        """This methods adds a list of items to molecular section."""
        for item in items:
            self.add(items)
        return self

    def get_items_number(self):
        """This method returns number of items within the molecular section."""
        return len(self.items)

    def __str__(self):
        """This method defines string conversion of a molecular section instance."""
        out = self.name + "\n\n"
        for item in self.items:
            out += str(item) + '\n'
        return out

    def __eq__(self, other):
        """This method defines equal '=' operator between two molecular section instances."""
        if not isinstance(other, MolecularSection):
            AssertionError("Expected %s for '=' operator!" % self.__class__.__name__)
        # set name and items
        self.__name = other.name
        self.__items = deepcopy(other.items)
        return self


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


# if __name__ == '__main__':

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