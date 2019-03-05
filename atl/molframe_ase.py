"""
As an adaptor for ASE module
"""

from molframe_base import *


class AdaptorASE:

    def __init__(self, ase_object):
        self.ase_object= ase_object   # ase object including structural info
        self.sections = dict()  # dictionary of molecular frame sections

    def get_molecular_frame_sections(self):

        # Box Section
        box_sections = BoxSection()
        cell_info = self.ase_object.get_cell().diagonal()  # WARNING: only works for orthogonal cell!
        box = Box(xlo=0, xhi=cell_info[0], ylo=0, yhi=cell_info[1], zlo=0, zhi=cell_info[2])
        self.sections['Box'] = box

        # Atoms Section
        atom_positions = self.ase_object.get_positions()
        atom_labels = self.ase_object.get_chemical_symbols()
        atoms_section = AtomsSection()
        for aid, pos, label in zip(range(len(atom_labels)), atom_positions, atom_labels):
            atom = Atom(atom_id=aid+1, molecule_id=0, atom_type=0, q=0.0, x=pos[0], y=pos[1], z=pos[2], label=label)
            atoms_section.add(atom)
        self.sections["Atoms"] = atoms_section

        # returning the list of molecular frame sections
        return self.sections


