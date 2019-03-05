"""
Molecular frame class
"""

from molframe_ase import AdaptorASE


class MolecularFrame:

    def __init__(self):
        self.sections = []

    def import_ase(self, ase_structure):
        mf_sections = AdaptorASE().get_molecular_frame_sections(ase_structure)
        for sec in mf_sections:
            self.sections.append(sec)

    def __str__(self):
        out = 'Molecular Frame'
        for sec in self.sections:
            out += str(sec) + '\n'
        return out



# ==========================================================================================


if __name__ == '__main__':

    from ase.build import bulk
    crys = bulk('Cu', 'fcc', a=3.6, orthorhombic=True)

    from ase.build.supercells import make_supercell
    import numpy as np
    P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * 10
    crys_supcell = make_supercell(crys, P)

    mf = MolecularFrame()
    mf.import_ase(crys_supcell)
    print(mf)

