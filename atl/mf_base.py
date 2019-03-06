"""
Here we define different molecular bases used in molecular frame sections including
Atom, Bond, Angle, Dihedral, Impropers, Box, Mass, and MolType classes.
"""

from mf_error import int_ge_zero, float_ge_zero


class Atom:

    def __init__(self, atom_id, molecule_id, atom_type, q, x, y, z, imx=0, imy=0, imz=0, label=''):
        try:
            self.atom_id = int_ge_zero(atom_id)          # atom id
            self.molecule_id = int_ge_zero(molecule_id)  # molecule id
            self.atom_type = int_ge_zero(atom_type)      # atom type
            self.q = float(q)        # atom charge
            self.x = float(x)        # x-coordinate
            self.y = float(y)        # y-coordinate
            self.z = float(z)        # z-coordinate
            self.imx = int(imx)      # image index along-x
            self.imy = int(imy)      # image index along-y
            self.imz = int(imz)      # image index along-z
            self.label = str(label)  # atom label (string)

        except ValueError:
            raise AssertionError("Unexpected value for Atom!")

    def __str__(self):
        out = ''
        for attribute in [self.atom_id, self.molecule_id, self.atom_type, self.q, self.x, self.y, self.z,
                          self.imx, self.imy, self.imz, self.label]:
            out += str(attribute) + ' '
        return out


class Bond:

    def __init__(self, bond_id, bond_type, aid_i, aid_j, label=''):
        try:
            self.bond_id = int_ge_zero(bond_id)      # bond id
            self.bond_type = int_ge_zero(bond_type)  # bond type
            self.aid_i = int_ge_zero(aid_i)  # atom id (i)
            self.aid_j = int_ge_zero(aid_j)  # atom id (j)
            self.label = str(label)          # bond label

        except ValueError:
            raise AssertionError("Unexpected value for Bond!")

    def __str__(self):
        out = ''
        for attribute in [self.bond_id, self.bond_type, self.aid_i, self.aid_j, self.label]:
            out += str(attribute) + ' '
        return out


class Angle:

    def __init__(self, angle_id, angle_type, aid_i, aid_j, aid_k, label=''):
        try:
            self.angle_id = int_ge_zero(angle_id)      # angle id
            self.angle_type = int_ge_zero(angle_type)  # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Angle!")

    def __str__(self):
        out = ''
        for attribute in [self.angle_id, self.angle_type, self.aid_i, self.aid_j, self.aid_j, self.label]:
            out += str(attribute) + ' '
        return out


class Dihedral:

    def __init__(self, dihedral_id, dihedral_type, aid_i, aid_j, aid_k, aid_l, label=''):
        try:
            self.dihedral_id = int_ge_zero(dihedral_id)        # angle id
            self.dihedral_type = int_ge_zero(dihedral_type)    # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.aid_l = int_ge_zero(aid_l)    # atom id (l)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Dihedral!")

    def __str__(self):
        out = ''
        for attribute in [self.dihedral_id, self.dihedral_type, self.aid_i, self.aid_j, self.aid_j, self.aid_l, self.label]:
            out += str(attribute) + ' '
        return out


class Improper:

    def __init__(self, improper_id, improper_type, aid_i, aid_j, aid_k, aid_l, label=''):
        try:
            self.improper_id = int_ge_zero(improper_id)        # angle id
            self.improper_type = int_ge_zero(improper_type)      # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.aid_l = int_ge_zero(aid_l)    # atom id (l)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Improper!")

    def __str__(self):
        out = ''
        for attribute in [self.improper_id, self.improper_type, self.aid_i, self.aid_j, self.aid_j, self.aid_l, self.label]:
            out += str(attribute) + ' '
        return out


class Mass:

    def __init__(self, mass_id, mass, label=''):
        try:
            self.mass_id = int_ge_zero(mass_id)  # mass id
            self.mass = float_ge_zero(mass)      # mass value
            self.label = str(label)              # mass label

        except ValueError:
            raise AssertionError("Unexpected value for Mass!")

    def __str__(self):
        out = ''
        for attribute in [self.mass_id, self.mass, self.label]:
            out += str(attribute) + ' '
        return out


class Box:

    def __init__(self, xlo, xhi, ylo, yhi, zlo, zhi, xy=0.0, xz=0.0, yz=0.0):
        try:
            box_dict = dict()
            box_dict['xlo xhi'] = [float(xlo), float(xhi)]  # box min&max along x-axis
            box_dict['ylo yhi'] = [float(ylo), float(yhi)]  # box min&max along y-axis
            box_dict['zlo zhi'] = [float(zlo), float(zhi)]  # box min&max along z-axis
            box_dict['xy xz yz'] = [float(xy), float(xz), float(yz)]  # tilted box
            self.box_dict = box_dict

        except ValueError:
            raise AssertionError("Unexpected value for Box!")

    def __str__(self):
        out = ''
        for key, value in self.box_dict.items():
            for num in value:
                out += str(num) + ' '
            out += key + '\n'
        return out


class MolType:

    def __init__(self, atoms=[0, 0], angles=[0, 0], bonds=[0, 0], dihedrals=[0, 0], impropers=[0, 0]):
        try:
            moltype_dict = dict()
            for add_text, index in [('s', 0), (' types', 1)]:  # loop over numbers & types
                moltype_dict['atom'+add_text] = int_ge_zero(atoms[index])
                moltype_dict['bond'+add_text] = int_ge_zero(bonds[index])
                moltype_dict['angle'+add_text] = int_ge_zero(angles[index])
                moltype_dict['dihedral'+add_text] = int_ge_zero(dihedrals[index])
                moltype_dict['improper'+add_text] = int_ge_zero(impropers[index])
            self.mtype_dict = moltype_dict

        except (ValueError, IndexError):
            raise AssertionError("Unexpected value for MolType!")

    def __str__(self):
        out = ''
        for key, value in self.mtype_dict.items():
                out += str(value) + ' ' + key + '\n'
        return out