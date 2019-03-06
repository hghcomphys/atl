"""
As an adaptor for ASE module
"""

from mf_section import *


class Adaptor:

    def __init__(self, package):
        self.package = package  # external package object including structural info
        self.sections = dict()  # dictionary of molecular sections

    # static method, this is implicitly a class method
    def make(self, package_name):
        try:
            # subclass name has to start with "Formatter"!
            formatter = eval("Adaptor" + str(package_name))(self.package)

        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected type for Formatter!")
        return formatter


class AdaptorASE(Adaptor):

    def get_molecular_sections(self):

        # Box Section
        box_sections = BoxSection()
        cell_info = self.package.get_cell().diagonal()  # WARNING: only works for orthogonal cell!
        box = Box(xlo=0, xhi=cell_info[0], ylo=0, yhi=cell_info[1], zlo=0, zhi=cell_info[2])
        self.sections['Box'] = box

        # Atoms Section
        atom_positions = self.package.get_positions()
        atom_labels = self.package.get_chemical_symbols()
        atoms_section = AtomsSection()
        for aid, pos, label in zip(range(len(atom_labels)), atom_positions, atom_labels):
            atom = Atom(atom_id=aid+1, molecule_id=0, atom_type=0, q=0.0, x=pos[0], y=pos[1], z=pos[2], label=label)
            atoms_section.add(atom)
        self.sections["Atoms"] = atoms_section

        # returning the list of molecular frame sections
        return self.sections

