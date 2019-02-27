"""
Defining molecular sections meta-class and subsequent classes

"""

from abc import	ABCMeta, abstractmethod


class MolFrameSection(metaclass=ABCMeta):

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Atom():

    def __init__(self, aid, mid, t, q, x, y, z, imx=0, imy=0, imz=0, tag=''):

        try:
            self.aid = int(aid)  # atom id
            self.mid = int(mid)  # molecules id
            self.t = int(t)      # types (number)

            # avoid not allowed negative inputs
            for arg in [self.aid, self.mid, self.t]:
                if arg < 0.0:
                    raise AssertionError("Unexpected value for Atom!")

            self.q = float(q)    # charges
            self.x = float(x)    # x-coordinates
            self.y = float(y)    # y-coordinates
            self.z = float(z)    # z-coordinates
            self.imx = int(imx)
            self.imy = int(imy)
            self.imz = int(imz)
            self.tag = str(tag)

        except ValueError:
            raise AssertionError("Unexpected value for Atom!")


class Atoms(MolFrameSection):

    def __init__(self):
        self.atoms = []

    def add_atom(self, atom):
        self.atoms.append(atom)

    def get_data(self):
        return self.atoms


# class Bonds(MolFrameSection):
#
#     def get_data(self):
#         return "Bonds data"
#
#
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
    obj = Atom(aid='-1', mid=1, t=1, q=0, x=0, y=0, z=0, imx=0, imy=0, imz=0, tag='')
    print('hi')

