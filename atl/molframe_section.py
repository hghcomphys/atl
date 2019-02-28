"""
Defining molecular sections meta-class and subsequent classes

"""

#from abc import	ABCMeta, abstractmethod
from atl.error import int_ge_zero


class MolFrameBlock:
    """
    Defining base class for each molecular frame block.
    """

    def __init__(self, name):
        self.items = []
        self.name = name

    def add(self, item):
        self.items.append(item)

    def get_list(self):
        return self.items

    def __str__(self):
        out = self.name + "\n\n"
        for atom in self.items:
            out += str(atom) + '\n'
        return out


class AtomsBlock(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Atoms')


class BondsBlock(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Bonds')


class AnglesBlock(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Angles')


class DihedralsBlock(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Dihedrals')


class ImpropersBlock(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Impropers')


# class Box(MolFrameSection):
#
#     def get_data(self):
#         return "Box data"
#
#
# class Masses(MolFrameSection):
#
#     def get_data(self):
#         return "Masses data"
#
#
# class Types(MolFrameSection):
#
#     def get_data(self):
#         return "Masses data"

class Atom:

    def __init__(self, aid, mid, atype, q, x, y, z, imx=0, imy=0, imz=0, label=''):
        try:
            self.aid = int_ge_zero(aid)     # atom id
            self.mid = int_ge_zero(mid)     # molecule id
            self.atype = int_ge_zero(atype) # atom type
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
        for attribute in [self.aid, self.mid, self.atype, self.q, self.x, self.y, self.z,
                          self.imx, self.imy, self.imz, self.label]:
            out += str(attribute) + ' '
        return out


class Bond:

    def __init__(self, bid, btype, aid_i, aid_j, label=''):

        try:
            self.bid = int_ge_zero(bid)      # bond id
            self.btype = int_ge_zero(btype)  # bond type
            self.aid_i = int_ge_zero(aid_i)  # atom id (i)
            self.aid_j = int_ge_zero(aid_j)  # atom id (j)
            self.label = str(label)          # bond label

        except ValueError:
            raise AssertionError("Unexpected value for Bond!")

    def __str__(self):
        out = ''
        for attribute in [self.bid, self.btype, self.aid_i, self.aid_j, self.label]:
            out += str(attribute) + ' '
        return out


class Angle:

    def __init__(self, anid, antype, aid_i, aid_j, aid_k, label=''):

        try:
            self.anid = int_ge_zero(anid)      # angle id
            self.antype = int_ge_zero(antype)  # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Angle!")

    def __str__(self):
        out = ''
        for attribute in [self.anid, self.antype, self.aid_i, self.aid_j, self.aid_j, self.label]:
            out += str(attribute) + ' '
        return out


class Dihedral:

    def __init__(self, did, dtype, aid_i, aid_j, aid_k, aid_l, label=''):

        try:
            self.did = int_ge_zero(did)        # angle id
            self.dtype = int_ge_zero(dtype)    # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.aid_l = int_ge_zero(aid_l)    # atom id (l)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Dihedral!")

    def __str__(self):
        out = ''
        for attribute in [self.did, self.dtype, self.aid_i, self.aid_j, self.aid_j, self.aid_l, self.label]:
            out += str(attribute) + ' '
        return out


class Improper:

    def __init__(self, iid, itype, aid_i, aid_j, aid_k, aid_l, label=''):

        try:
            self.iid = int_ge_zero(iid)        # angle id
            self.itype = int_ge_zero(itype)    # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.aid_l = int_ge_zero(aid_l)    # atom id (l)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Improper!")

    def __str__(self):
        out = ''
        for attribute in [self.iid, self.itype, self.aid_i, self.aid_j, self.aid_j, self.aid_l, self.label]:
            out += str(attribute) + ' '
        return out






if __name__ == '__main__':

    atom1 = Atom(aid=1, mid=1, atype=1, q=0, x=0.3, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atom2 = Atom(aid=2, mid=1, atype=1, q=0, x=0.5, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atoms_block = AtomsBlock()
    atoms_block.add(atom1)
    atoms_block.add(atom2)
    print (atoms_block)

    bond1 = Bond(bid=1, btype=1, aid_i=1, aid_j=2)
    bond2 = Bond(bid=2, btype=1, aid_i=1, aid_j=2)
    bonds_block = BondsBlock()
    bonds_block.add(bond1)
    bonds_block.add(bond2)
    print (bonds_block)

    angle1 = Angle(anid=1, antype=1, aid_i=2, aid_j=4, aid_k=5, label=' # water angle')
    angles_block = AnglesBlock()
    angles_block.add(angle1)
    print (angles_block)

    dihedral1 = Dihedral(did=1, dtype=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    dihedral_block = DihedralsBlock()
    dihedral_block.add(dihedral1)
    print (dihedral_block)

    # Atoms = MolFrameBlock('Atoms')
    # Atoms.add()
    # Atoms.data()
    # Atoms


