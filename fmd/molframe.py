""" Molecular Frame

Molecular frame contains collection of atoms in form of molecular topology and simulation box data.
It is described in a dictionary of molecular sections that basically includes list of Atom, Box, Masses, etc.
It can import (export) molecular structure from (to) external packages (i.e. ASE), having methods
to read & write files in desired format (such as .xyz), selecting specific group of atoms,
and methods for integrating two molecular frame instances.
"""

from .molsection import MolecularSection, AtomsSection
from .adaptor import Adaptor
from .formatter import Formatter
from copy import deepcopy


class MolecularFrame:
    """Molecular Frame"""

    def __init__(self, name='Molecular Frame', molecular_sections=None):
        """makes a new instance of molecular frame"""
        self.name = name  # assign a given name for molecular frame
        self.__molecular_sections = dict()  # initialize molecular sections as a dictionary
        # initialize molecular sections
        if isinstance(molecular_sections, dict):
            self.set_molecular_sections(molecular_sections)
        elif molecular_sections is not None:
            self.set_molecular_section(molecular_sections)

    @property
    def name(self):
        """returns molecular frame name"""
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = str(name)

    @property
    def molecular_sections(self):
        """This method returns all molecular sections in form of a dictionary."""
        return self.__molecular_sections

    def __str__(self):
        """A method that defines string conversion for a molecular frame instance."""
        out = self.__name + '\n'
        for mol_sec in self.__molecular_sections.values():
            out += str(mol_sec) + '\n'
        return out

    def get_molecular_section(self, section_name):
        """A method that returns an specified molecular section by giving its name (key)."""
        if section_name not in self.molecular_sections.keys():
            raise AssertionError("Cannot find section name for %s!" % self.get_molecular_section.__name__)
        return self.__molecular_sections[section_name]

    def set_molecular_section(self, molecular_section):
        """This method sets a specified molecular section into molecular frame."""
        if not isinstance(molecular_section, MolecularSection):
            raise AssertionError("Unexpected given molecular section for %s!" % self.__class__.__name__)
        self.__molecular_sections[molecular_section.name] = molecular_section

    def set_molecular_sections(self, molecular_sections):
        """This method sets input molecular sections in form of a dictionary."""
        if not isinstance(molecular_sections, dict):
            raise AssertionError("Expected dict input argument for %s!" % self.set_molecular_sections.__name__)
        # assign all molecular sections
        for mol_sec in molecular_sections.values():
            self.set_molecular_section(mol_sec)

    def get_atoms(self):
        """Returns atoms section"""
        return self.get_molecular_section("Atoms").atoms

    def get_atoms_number(self):
        """Returns number of atoms"""
        return len(self.get_atoms())

    def import_from(self, package_instance, package_name="ASE"):
        """This method imports molecular frame from an external module such as ASE."""
        # TODO: default package name is set to "ASE"!
        # TODO: error handling for a given input package
        self.set_molecular_sections(Adaptor(package_instance).make(package_name).get_molecular_sections())
        return self

    def read(self, file_name, file_format='xyz'):
        """This method reads a file with specified format into molecular frame."""
        self.set_molecular_sections(Formatter(self).make(file_format.upper()).read(file_name))
        return self

    def write(self, file_name, file_format='xyz'):
        """A method that writes molecular frame into a file with given format."""
        Formatter(self).make(file_format.upper()).write(file_name)

    def __eq__(self, other):
        """This method defines equal '=' operator between two molecular frame instances."""
        if not isinstance(other, MolecularFrame):
            raise AssertionError("Expected %s for '=' operator!" % self.__class__.__name__)
        # set name and molecular sections from 'other' instance
        self.name = other.name
        self.set_molecular_sections(deepcopy(other.molecular_sections))
        return self

    def __add__(self, other):
        """This method defines '+' operator between two molecular frame instances."""
        if not isinstance(other, MolecularFrame):
            raise AssertionError("Expected %s for '+' operator!" % self.__class__.__name__)
        # make a new molecular frame by integrating two given ones
        new_mf = MolecularFrame(self.name + ' + ' + other.name)
        # TODO: it only works for Atoms!
        for mol_sec in ["Atoms"]:
            new_mf.set_molecular_section(self.get_molecular_section(mol_sec) + other.get_molecular_section(mol_sec))
        return new_mf

    def select_atoms_region(self, region_fn=None):
        """This method returns a new molecular frame includes atoms which specified by input function region_fn."""
        if region_fn is None:
            raise AssertionError("Expected region function argument for %s!" % self.select_atoms_region.__name__)
        # make a new molecular frame
        new_mf = MolecularFrame(self.name + '(%s)' % region_fn.__name__)
        # make a new atom section and select atoms base on region_fn
        atom_section = AtomsSection()
        for atom in self.get_molecular_section("Atoms").atoms:
            if region_fn(atom.x, atom.y, atom.z):
                atom_section.add(atom)
        # set selected atoms section to new molecular frame
        new_mf.set_molecular_section(deepcopy(atom_section))
        # TODO: it only works for Atoms!
        # return new molecular frame
        return new_mf

    def export_to(self):
        """This method exports molecular frame as an specified external package instance such as ASE."""
        pass




