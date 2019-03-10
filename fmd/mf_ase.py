"""
As an adaptor for ASE module
"""

from mf_atom import Atom, AtomsSection
from mf_box import Box, BoxSection


class Adaptor:

    def __init__(self, package_instance):
        self._package_instance = package_instance  # external package object including structural info
        self._molecular_sections = dict()  # dictionary of molecular sections

    def _set_molecular_section(self, molecular_section):
        self._molecular_sections[molecular_section.name] = molecular_section

    # static method, this is implicitly a class method
    def make(self, package_name):
        try:
            # subclass name has to start with "Formatter"!
            formatter = eval("Adaptor" + str(package_name))(self._package_instance)

        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected type for Formatter!")
        return formatter


class AdaptorASE(Adaptor):

    def get_molecular_sections(self):

        # Box Section
        box_section = BoxSection()
        cell_info = self._package_instance.get_cell().diagonal()  # WARNING: only works for orthogonal cell!
        box = Box(xlo=0, xhi=cell_info[0], ylo=0, yhi=cell_info[1], zlo=0, zhi=cell_info[2])
        box_section.add(box)
        self._set_molecular_section(box_section)

        # Atoms Section
        atom_positions = self._package_instance.get_positions()
        atom_labels = self._package_instance.get_chemical_symbols()
        atoms_section = AtomsSection()
        for aid, pos, label in zip(range(len(atom_labels)), atom_positions, atom_labels):
            atom = Atom(atom_id=aid+1, molecule_id=0, atom_type=0, q=0.0, x=pos[0], y=pos[1], z=pos[2], label=label)
            atoms_section.add(atom)
        self._set_molecular_section(atoms_section)

        # returning a dictionary of molecular frame sections
        return self._molecular_sections

