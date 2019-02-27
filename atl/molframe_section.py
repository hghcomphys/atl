"""
Defining molecular sections meta-class and subsequent classes

"""

from abc import	ABCMeta, abstractmethod


class MolFrameSection(metaclass=ABCMeta):

    @abstractmethod
    def get_data(self):
        pass

    # @abstractmethod
    # def set_data(self):
    #     pass


def int_ge_zero(n):

    int_n = int(n)
    if int_n < 0:
        AssertionError("Unexpected negative value!")
    else:
        return int_n


class Atom:

    def __init__(self, aid, mid, typ, q, x, y, z, imx=0, imy=0, imz=0, tag=''):

        try:
            self.aid = int_ge_zero(aid)  # atom id
            self.mid = int_ge_zero(mid)  # molecules id
            self.typ = int_ge_zero(typ)  # atom type
            self.q = float(q)    # charge
            self.x = float(x)    # x-coordinates
            self.y = float(y)    # y-coordinates
            self.z = float(z)    # z-coordinates
            self.imx = int(imx)  # image index along-x
            self.imy = int(imy)  # image index along-y
            self.imz = int(imz)  # image index along-z
            self.tag = str(tag)  # atom tag (string)

        except ValueError:
            raise AssertionError("Unexpected value for Atom!")

    def __str__(self):
        out = ''
        for attribute in [self.aid, self.mid, self.typ, self.q, self.x, self.y, self.z, self.imx, self.imy, self.imz, self.tag]:
            out += str(attribute)+' '
        return out


class Atoms(MolFrameSection):

    def __init__(self):
        self.atoms = []

    def add_atom(self, atom):
        self.atoms.append(atom)

    def get_data(self):
        return self.atoms


class Bond:

    def __init__(self, bid, typ, aid_i, aid_j):

        try:
            self.bid = int_ge_zero(bid)     # bond id
            self.typ = int_ge_zero(typ)     # bond type
            self.aid_i = int_ge_zero(aid_i) # atom id (i)
            self.aid_j = int_ge_zero(aid_j) # atom id (j)

        except ValueError:
            raise AssertionError("Unexpected value for Bond!")

    def __str__(self):
        out = ''
        for attribute in [self.bid, self.typ, self.aid_i, self.aid_j]:
            out += str(attribute) + ' '
        return out


class Bonds(MolFrameSection):

        def __init__(self):
            self.bonds = []

        def add_bond(self, bond):
            self.bonds.append(bond)

        def get_data(self):
            return self.bonds


# class Angles(MolFrameSection):
#
#     def get_data(self):
#         return "Angles data"
#
#
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

    atom1 = Atom(aid=1, mid=1, typ=1, q=0, x=0.3, y=0, z=0, imx=0, imy=0, imz=0, tag='')
    atom2 = Atom(aid=2, mid=1, typ=1, q=0, x=0.5, y=0, z=0, imx=0, imy=0, imz=0, tag='')

    sec_atoms = Atoms()
    sec_atoms.add_atom(atom1)
    sec_atoms.add_atom(atom2)


    bond1 = Bond(bid=1, typ=1, aid_i=1, aid_j=2)
    bond2 = Bond(bid=2, typ=1, aid_i=1, aid_j=2)

    sec_bonds = Bonds()
    sec_bonds.add_bond(bond1)
    sec_bonds.add_bond(bond2)

    # for atm in sec_atoms.get_data():
    #     print(atm)

    for bnd in sec_bonds.get_data():
        print(bnd)



