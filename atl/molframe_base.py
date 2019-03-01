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

    # static method, this is implicitly a class method
    def make(block_object_name):
        try:
            block_object = eval(str(block_object_name))()

        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected type for MolFrameBlock!")
        return block_object


class Atoms(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Atoms')


class Bonds(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Bonds')


class Angles(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Angles')


class Dihedrals(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Dihedrals')


class Impropers(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Impropers')


class Box(MolFrameBlock):

    def __init__(self):
        MolFrameBlock.__init__(self, 'Box')
        self.items = None  # always len(items)==1

    def add(self, cell_obj):
        if isinstance(cell_obj, Cell):
            self.items = cell_obj
        else:
            raise AssertionError("Unexpected type for Box!")

    def __str__(self):
        return str(self.items)


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

    def __init__(self, aid, mid, typ, q, x, y, z, imx=0, imy=0, imz=0, label=''):
        try:
            self.aid = int_ge_zero(aid)     # atom id
            self.mid = int_ge_zero(mid)     # molecule id
            self.typ = int_ge_zero(typ)     # atom type
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
        for attribute in [self.aid, self.mid, self.typ, self.q, self.x, self.y, self.z,
                          self.imx, self.imy, self.imz, self.label]:
            out += str(attribute) + ' '
        return out


class Bond:

    def __init__(self, bid, typ, aid_i, aid_j, label=''):
        try:
            self.bid = int_ge_zero(bid)      # bond id
            self.typ = int_ge_zero(typ)      # bond type
            self.aid_i = int_ge_zero(aid_i)  # atom id (i)
            self.aid_j = int_ge_zero(aid_j)  # atom id (j)
            self.label = str(label)          # bond label

        except ValueError:
            raise AssertionError("Unexpected value for Bond!")

    def __str__(self):
        out = ''
        for attribute in [self.bid, self.typ, self.aid_i, self.aid_j, self.label]:
            out += str(attribute) + ' '
        return out


class Angle:

    def __init__(self, anid, typ, aid_i, aid_j, aid_k, label=''):
        try:
            self.anid = int_ge_zero(anid)      # angle id
            self.typ = int_ge_zero(typ)        # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Angle!")

    def __str__(self):
        out = ''
        for attribute in [self.anid, self.typ, self.aid_i, self.aid_j, self.aid_j, self.label]:
            out += str(attribute) + ' '
        return out


class Dihedral:

    def __init__(self, did, typ, aid_i, aid_j, aid_k, aid_l, label=''):
        try:
            self.did = int_ge_zero(did)        # angle id
            self.typ = int_ge_zero(typ)        # angle type
            self.aid_i = int_ge_zero(aid_i)    # atom id (i)
            self.aid_j = int_ge_zero(aid_j)    # atom id (j)
            self.aid_k = int_ge_zero(aid_k)    # atom id (k)
            self.aid_l = int_ge_zero(aid_l)    # atom id (l)
            self.label = str(label)

        except ValueError:
            raise AssertionError("Unexpected value for Dihedral!")

    def __str__(self):
        out = ''
        for attribute in [self.did, self.typ, self.aid_i, self.aid_j, self.aid_j, self.aid_l, self.label]:
            out += str(attribute) + ' '
        return out


class Improper:

    def __init__(self, iid, typ, aid_i, aid_j, aid_k, aid_l, label=''):
        try:
            self.iid = int_ge_zero(iid)        # angle id
            self.itype = int_ge_zero(typ)      # angle type
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


class Cell:

    def __init__(self, xlo, xhi, ylo, yhi, zlo, zhi, xy=0.0, xz=0.0, yz=0.0):
        try:
            # cell min&max along x-axis
            self.xlo = float(xlo)
            self.xhi = float(xhi)
            # cell min&max along y-axis
            self.ylo = float(ylo)
            self.yhi = float(yhi)
            # cell min&max along z-axis
            self.zlo = float(zlo)
            self.zhi = float(zhi)
            # tilted box
            self.xy = float(xy)
            self.xz = float(xz)
            self.yz = float(yz)

        except ValueError:
            raise AssertionError("Unexpected value for Cell!")

    def get_cell_dict(self):
        """
        return cell in format of dictionary
        """
        cell = dict()
        cell['xlo xhi'] = [self.xlo, self.xhi]  # box min&max along x-axis
        cell['ylo yhi'] = [self.ylo, self.yhi]  # box min&max along y-axis
        cell['zlo zhi'] = [self.zlo, self.xhi]  # box min&max along z-axis
        cell['xy xz yz'] = [self.xy, self.xz, self.yz]  # tilted box
        return cell

    def __str__(self):
        out = ''
        for key, value in self.get_cell_dict().items():
            for num in value:
                out += str(num) + ' '
            out += key + '\n'
        return out




# ==========================================================================================

if __name__ == '__main__':

    atom1 = Atom(aid=1, mid=1, typ=1, q=0, x=0.3, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atom2 = Atom(aid=2, mid=1, typ=1, q=0, x=0.5, y=0, z=0, imx=0, imy=0, imz=0, label='')
    atoms_block = MolFrameBlock.make('Atoms')
    atoms_block.add(atom1)
    atoms_block.add(atom2)
    print (atoms_block)

    bond1 = Bond(bid=1, typ=1, aid_i=1, aid_j=2)
    bond2 = Bond(bid=2, typ=1, aid_i=1, aid_j=2)
    bonds_block = Bonds()
    bonds_block.add(bond1)
    bonds_block.add(bond2)
    print (bonds_block)

    angle1 = Angle(anid=1, typ=1, aid_i=2, aid_j=4, aid_k=5, label=' # water angle')
    angles_block = Angles()
    angles_block.add(angle1)
    print (angles_block)

    dihedral1 = Dihedral(did=1, typ=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    dihedral_block = Dihedrals()
    dihedral_block.add(dihedral1)
    print (dihedral_block)

    improper1 = Improper(iid=1, typ=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    improper_block = Impropers()
    improper_block.add(improper1)
    print (improper_block)

    cell1 = Cell(xlo=1, xhi=2, ylo=-1, yhi=2.3, zlo=92, zhi=23)
    box_block = Box() #MolFrameBlock.make("Box")
    box_block.add(cell1)
    print (box_block)



