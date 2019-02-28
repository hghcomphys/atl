"""
Defining molecular sections meta-class and subsequent classes

"""

from abc import	ABCMeta, abstractmethod


class MolFrameBlock(metaclass=ABCMeta):

    # @abstractmethod
    # def __init__(self):
    #     pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get_list(self):
        pass

    # @abstractmethod
    # def set_data(self):
    #     pass

    @abstractmethod
    def __str__(self):
        pass


def int_ge_zero(n):

    int_n = int(n)
    if int_n < 0:
        AssertionError("Unexpected negative value!")
    else:
        return int_n


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


class AtomsBlock(MolFrameBlock):

    def __init__(self):
        self.atoms = []

    def add(self, atom):
        self.atoms.append(atom)

    def get_list(self):
        return self.atoms

    def __str__(self):
        out = "Atoms\n\n"
        for atom in self.atoms:
            out += str(atom) + '\n'
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


class BondsBlock(MolFrameBlock):

        def __init__(self):
            self.bonds = []

        def add(self, bond):
            self.bonds.append(bond)

        def get_list(self):
            return self.bonds

        def __str__(self):
            out = "Bonds\n\n"
            for bond in self.bonds:
                out += str(bond) + '\n'
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


class AnglesBlock(MolFrameBlock):

    def __init__(self):
        self.angles = []

    def add(self, angle):
        self.angles.append(angle)

    def get_list(self):
        return self.angles

    def __str__(self):
        out = "Angles\n\n"
        for angle in self.angles:
            out += str(angle) + '\n'
        return out


# class Dihedrals(MolFrameSection):
#
#     def get_data(self):
#         return "Dihedrals data"
#
#
# class Impropers(MolFrameSection):
#
#     def get_data(self):
#         return "Impropers data"
#
#
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

    # Atoms = MolFrameBlock('Atoms')
    # Atoms.add()
    # Atoms.data()
    # Atoms


