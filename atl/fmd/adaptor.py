"""Adaptor for external package"""

from .atom import Atom
from .box import Box, BoxSection


class Adaptor:
    """General base class for external package adaptor"""

    def __init__(self, package_instance):
        self.__package_instance = package_instance  # external package object including structural info
        self.__adaptor_molecular_sections = dict()  # dictionary of molecular sections

    @property
    def package_instance(self):
        """returns external package name"""
        return self.__package_instance

    @property
    def adaptor_molecular_sections(self):
        """returns adaptor molecular sections"""
        return self.__adaptor_molecular_sections

    def make(self, package_name):
        """This method creates an appropriate adaptor instance."""
        try:
            # subclass name has to start with "Formatter"!
            formatter = eval("Adaptor" + str(package_name))(self.package_instance)
        # catch possible error
        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected type for Formatter!")
        # returns a created instance of desired adaptor
        return formatter


class AdaptorASE(Adaptor):
    """Adaptor for ASE package"""

    def get_molecular_sections(self):
        """This method returns molecular sections imported though ASE adaptor."""

        # Box Section
        box_section = BoxSection()
        cell_info = self.package_instance.get_cell().diagonal()
        # TODO: only works for orthogonal cell!
        box = Box(xlo=0, xhi=cell_info[0], ylo=0, yhi=cell_info[1], zlo=0, zhi=cell_info[2])
        box_section.add(box)
        self.adaptor_molecular_sections[box_section.name] = box_section

        # Atoms Section
        atom_positions = self.package_instance.get_positions()
        atom_labels = self.package_instance.get_chemical_symbols()
        atoms_section = AtomsSection()
        for aid, pos, label in zip(range(len(atom_labels)), atom_positions, atom_labels):
            atom = Atom(atom_id=aid+1, molecule_id=0, atom_type=0, q=0.0, x=pos[0], y=pos[1], z=pos[2], label=label)
            atoms_section.add(atom)
            self.adaptor_molecular_sections[atoms_section.name] = atoms_section

        # returning a dictionary of molecular frame sections
        return self.adaptor_molecular_sections


if __name__ == '__main__':
    # TODO: add tests here!
    print ("No test!")