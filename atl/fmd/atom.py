"""Atom"""

from .error import int_ge_zero


class Atom:
    """Atom class contains all info about atom and can be used in atom section as one type of molecular sections."""

    def __init__(self, x, y, z, label='UNK', atom_id=0, molecule_id=0, atom_type=0, q=0.0, imx=0, imy=0, imz=0):
        try:
            self.__atom_id = int_ge_zero(atom_id)  # atom id
            self.__molecule_id = int_ge_zero(molecule_id)  # molecule id
            self.__atom_type = int_ge_zero(atom_type)  # atom type
            self.__q = float(q)  # atom charge
            self.x = x  # x-coordinate
            self.y = y  # y-coordinate
            self.z = z  # z-coordinate
            self.__imx = int(imx)  # image index along-x
            self.__imy = int(imy)  # image index along-y
            self.__imz = int(imz)  # image index along-z
            self.label = label  # atom label (string)

        except (ValueError):
            raise AssertionError("Unexpected value for initializing %s!" % self.__class__.__name__)

    @property
    def x(self):
        """returns x position of atom"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x position of atom"""
        self.__x = float(x)

    @property
    def y(self):
        """returns y position of atom"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y position of atom"""
        self.__y = float(y)

    @property
    def z(self):
        """returns z position of atom"""
        return self.__z

    @z.setter
    def z(self, z):
        """set z position of atom"""
        self.__z = float(z)

    @property
    def label(self):
        """return given label for atom"""
        return self.__label

    @label.setter
    def label(self, label):
        """set given label for atom"""
        self.__label = str(label)

    def __str__(self):
        """defines string conversion for Atom"""
        out = ''
        # for attribute in [self.__atom_id, self.__molecule_id, self.__atom_type, self.__q, self.__x, self.__y,
        #                   self.__z, self.__imx, self.__imy, self.__imz, self.__label]:
        # TODO: string conversion only shows x, y, z, label of the atom!
        for attribute in [self.label, self.x, self.y, self.z]:
            out += str(attribute) + ' '
        return out


