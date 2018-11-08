
def write_xyz(atom_txyz=[], filename='atl-dump.xyz'):
    """
    This function writes 2D-data into a .xyz file.
    """

    nAtoms = len(atom_txyz)
    fout = open(filename, 'w')
    fout.write("%d\n" % nAtoms)
    fout.write("ATL-dump\n")
    for i in range(nAtoms):
        fout.write(
            "%s %20.15f %20.15f %20.15f\n"%(atom_txyz[i][0], atom_txyz[i][1], atom_txyz[i][2], atom_txyz[i][3]))
    fout.close()