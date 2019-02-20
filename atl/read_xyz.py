"""
Reading lammps data frame into an array or pandas data format
"""

import pandas

def read_xyz(filename='dump.xyz', frame=-1):
    """
    This function reads specific frame of a *.xyz file and returns
    the data as 2D-list.

    Example:

        atoms=read_xyz(path+'grn.xyz')
    """
    nAtoms = 0
    nFrame = 0
    with open(filename, 'r') as fp:
        for line in fp:

            if not line:
                break

            atom_txyz = []
            nAtoms = int(line)
            next(fp)
            nFrame += 1
            if nFrame >= frame:
                for i in range(nAtoms):
                    line = next(fp)
                    line = line.rstrip("/n").split()
                    atom_txyz.append([line[0], float(line[1]), float(line[2]), float(line[3])])
            else:
                for i in range(nAtoms):
                    next(fp)
            if (frame > 0) and (nFrame >= frame):
                break

    return atom_txyz


# ========================================================================================


def read_xyz_pandas(filename='dump.xyz', frame=-1):
    """
    This function reads specific frame of a *.xyz file and returns
    the data as pandas data frame.

    Example:

        df = atl.read_xyz_pandas(filename='dump.xyz',frame=-1)
        df.head()
    """
    atoms = read_xyz(filename, frame)
    return pandas.DataFrame(atoms, columns=['t', 'x', 'y', 'z'])

