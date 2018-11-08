
def total_dipole(filename='water.xyz', type_charge_dict={'O': -0.834, 'H': 0.417}, frame_range=[-1,1,10]):
    """
    This function calculates the total dipole moment for a given range of frame [begin,end,step].
    Input atomic data is in .xyz format and it returns list of evaluated dipole moments.
    Atomic types and corresponding charges are specified as input dictionary.

    Example

        water={'O':-0.834,'H':0.417}
        P=total_dipole('../data/dump.xyz', type_charge_dict=water,frames=[1,-1,5]) # -1 indicates the last frame
    """

    from atl import read_xyz_pandas

    if frame_range[1]<1:
        frame_range[1]=1000000

    dipole = []
    for f in range(frame_range[0], frame_range[1] + 1, frame_range[2]):

        atoms = read_xyz_pandas(filename, f)
        if atoms.size == 0:
            break

        totP = 0.0
        for k in type_charge_dict.keys():
            totP += (atoms[atoms['t'] == k][['x', 'y', 'z']] * type_charge_dict[k]).sum()

        dipole.append(list(totP))

    return dipole