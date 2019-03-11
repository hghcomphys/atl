"""Defining molecular sections"""

from copy import deepcopy
from .atom import Atom


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
            print (type(atom), type(Atom), "hi")
            raise AssertionError("Expected Atom type for %s method!" % self.add.__name__)
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
