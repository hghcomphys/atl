"""Box base class

It contains all data related to the simulation box and can be used in box section as one type of molecular sections.
"""


class Box:

    def __init__(self, xlo, xhi, ylo, yhi, zlo, zhi, xy=0.0, xz=0.0, yz=0.0):
        try:
            box_dict = dict()  # an empty dictionary for all box data including lengths, angles, etc
            box_dict['xlo xhi'] = [float(xlo), float(xhi)]  # box min&max along x-axis
            box_dict['ylo yhi'] = [float(ylo), float(yhi)]  # box min&max along y-axis
            box_dict['zlo zhi'] = [float(zlo), float(zhi)]  # box min&max along z-axis
            box_dict['xy xz yz'] = [float(xy), float(xz), float(yz)]  # tilted box
            self.set_box_dict(box_dict)  # initialize box_dict variable

        except ValueError:
            raise AssertionError("Unexpected value for %s!" % self.__class__.__name__)

    def get_box_dict(self):
        """return box data in form of a dict"""
        return self.__box_dict

    def set_box_dict(self, box_dict=None):
        """set box data using input box dict"""
        if not isinstance(box_dict, dict):
            raise AssertionError("Expected  a dict type for %s!" % self.set_box_dict.__name__)
        self.__box_dict = box_dict

    def __str__(self):
        """string conversion of Box instance"""
        out = ''
        for key, value in self.__box_dict.items():
            for num in value:
                out += str(num) + ' '
            out += key + '\n'
        return out

    @property
    def lx(self):
        """It returns box length along x-axis"""
        l = self.get_box_dict()['xlo xhi']
        return l[1]-l[0]

    @property
    def ly(self):
        """It returns box length along y-axis"""
        l = self.get_box_dict()['ylo yhi']
        return l[1]-l[0]

    @property
    def lz(self):
        """It returns box length along z-axis"""
        l = self.get_box_dict()['zlo zhi']
        return l[1]-l[0]

    def get_volume(self):
        """This method returns box volume"""
        # TODO: only works for orthogonal box
        return self.lx*self.ly*self.lz
