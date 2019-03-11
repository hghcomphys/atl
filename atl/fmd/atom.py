"""Atom"""

from .error import int_ge_zero


class Atom:
    """Atom class contains all info about atom and can be used in atom section as one type of molecular sections."""

    def __init__(self, atom_id, molecule_id, atom_type, q, x, y, z, imx=0, imy=0, imz=0, label=''):
        try:
            self.__atom_id = int_ge_zero(atom_id)  # atom id
            self.__molecule_id = int_ge_zero(molecule_id)  # molecule id
            self.__atom_type = int_ge_zero(atom_type)  # atom type
            self.__q = float(q)  # atom charge
            self.__x = float(x)  # x-coordinate
            self.__y = float(y)  # y-coordinate
            self.__z = float(z)  # z-coordinate
            self.__imx = int(imx)  # image index along-x
            self.__imy = int(imy)  # image index along-y
            self.__imz = int(imz)  # image index along-z
            self.__label = str(label)  # atom label (string)

        except (ValueError):
            raise AssertionError("Unexpected value for initializing %s!" % self.__class__.__name__)

    @property
    def x(self):
        """returns x position of atom"""
        return self.__x

    @property
    def y(self):
        """returns y position of atom"""
        return self.__y

    @property
    def z(self):
        """returns z position of atom"""
        return self.__z

    @property
    def label(self):
        """return assigned label of atom"""
        return self.__label

    def __str__(self):
        """defines string conversion for Atom"""
        out = ''
        for attribute in [self.__atom_id, self.__molecule_id, self.__atom_type, self.__q, self.__x, self.__y, self.__z,
                          self.__imx, self.__imy, self.__imz, self.__label]:
            out += str(attribute) + ' '
        return out


