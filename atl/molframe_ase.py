"""
As an adaptor for ASE module
"""

from molframe_base import *


class AdaptorASE:

    def __init__(self):
        pass

    def get_molecular_frame_sections(self, ase_structure):

        mf_sections = []

        # importing sections from ase structure
        atom_positions = ase_structure.get_positions()
        atom_labels = ase_structure.get_chemical_symbols()
        atoms_section = AtomsSection()
        for aid, pos, label in zip(range(len(atom_labels)), atom_positions, atom_labels):
            atom = Atom(atom_id=aid+1, molecule_id=0, atom_type=0, q=0.0, x=pos[0], y=pos[1], z=pos[0], label=label)
            atoms_section.add(atom)
        mf_sections.append(atoms_section)

        # returning a list of molecular frame sections
        return mf_sections


