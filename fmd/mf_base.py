"""
Here we define different molecular bases used in molecular frame sections including
Atom, Bond, Angle, Dihedral, Impropers, Box, Mass, and MolType classes.
"""

# from mf_error import float_ge_zero


# class Bond:
#
#     def __init__(self, bond_id, bond_type, aid_i, aid_j, label=''):
#         try:
#             self._bond_id = int_ge_zero(bond_id)      # bond id
#             self._bond_type = int_ge_zero(bond_type)  # bond type
#             self._aid_i = int_ge_zero(aid_i)  # atom id (i)
#             self._aid_j = int_ge_zero(aid_j)  # atom id (j)
#             self._label = str(label)          # bond label
#
#         except ValueError:
#             raise AssertionError("Unexpected value for %s!" % self.__class__.__name__)
#
#     def __str__(self):
#         out = ''
#         for attribute in [self._bond_id, self._bond_type, self._aid_i, self._aid_j, self._label]:
#             out += str(attribute) + ' '
#         return out
#
#
# class Angle:
#
#     def __init__(self, angle_id, angle_type, aid_i, aid_j, aid_k, label=''):
#         try:
#             self._angle_id = int_ge_zero(angle_id)      # angle id
#             self._angle_type = int_ge_zero(angle_type)  # angle type
#             self._aid_i = int_ge_zero(aid_i)    # atom id (i)
#             self._aid_j = int_ge_zero(aid_j)    # atom id (j)
#             self._aid_k = int_ge_zero(aid_k)    # atom id (k)
#             self._label = str(label)
#
#         except ValueError:
#             raise AssertionError("Unexpected value for %s!" % self.__class__.__name__)
#
#     def __str__(self):
#         out = ''
#         for attribute in [self._angle_id, self._angle_type, self._aid_i, self._aid_j, self._aid_j, self._label]:
#             out += str(attribute) + ' '
#         return out
#
#
# class Dihedral:
#
#     def __init__(self, dihedral_id, dihedral_type, aid_i, aid_j, aid_k, aid_l, label=''):
#         try:
#             self._dihedral_id = int_ge_zero(dihedral_id)        # angle id
#             self._dihedral_type = int_ge_zero(dihedral_type)    # angle type
#             self._aid_i = int_ge_zero(aid_i)    # atom id (i)
#             self._aid_j = int_ge_zero(aid_j)    # atom id (j)
#             self._aid_k = int_ge_zero(aid_k)    # atom id (k)
#             self._aid_l = int_ge_zero(aid_l)    # atom id (l)
#             self._label = str(label)
#
#         except ValueError:
#             raise AssertionError("Unexpected value for %s!" % self.__class__.__name__)
#
#     def __str__(self):
#         out = ''
#         for attribute in [self._dihedral_id, self._dihedral_type, self._aid_i, self._aid_j,
#                           self._aid_j, self._aid_l, self._label]:
#             out += str(attribute) + ' '
#         return out
#
#
# class Improper:
#
#     def __init__(self, improper_id, improper_type, aid_i, aid_j, aid_k, aid_l, label=''):
#         try:
#             self._improper_id = int_ge_zero(improper_id)        # angle id
#             self._improper_type = int_ge_zero(improper_type)      # angle type
#             self._aid_i = int_ge_zero(aid_i)    # atom id (i)
#             self._aid_j = int_ge_zero(aid_j)    # atom id (j)
#             self._aid_k = int_ge_zero(aid_k)    # atom id (k)
#             self._aid_l = int_ge_zero(aid_l)    # atom id (l)
#             self._label = str(label)
#
#         except ValueError:
#             raise AssertionError("Unexpected value for %s!" % self.__class__.__name__)
#
#     def __str__(self):
#         out = ''
#         for attribute in [self._improper_id, self._improper_type, self._aid_i, self._aid_j,
#                           self._aid_j, self._aid_l, self._label]:
#             out += str(attribute) + ' '
#         return out
#
#
# class Mass:
#
#     def __init__(self, mass_id, mass, label=''):
#         try:
#             self._mass_id = int_ge_zero(mass_id)  # mass id
#             self._mass = float_ge_zero(mass)      # mass value
#             self._label = str(label)              # mass label
#
#         except ValueError:
#             raise AssertionError("Unexpected value for %s!" % self.__class__.__name__)
#
#     def __str__(self):
#         out = ''
#         for attribute in [self._mass_id, self._mass, self._label]:
#             out += str(attribute) + ' '
#         return out
#
#
# class MolType:
#
#     def __init__(self, atoms=[0, 0], angles=[0, 0], bonds=[0, 0], dihedrals=[0, 0], impropers=[0, 0]):
#         try:
#             moltype_dict = dict()
#             for add_text, index in [('s', 0), (' types', 1)]:  # loop over numbers & types
#                 moltype_dict['atom'+add_text] = int_ge_zero(atoms[index])
#                 moltype_dict['bond'+add_text] = int_ge_zero(bonds[index])
#                 moltype_dict['angle'+add_text] = int_ge_zero(angles[index])
#                 moltype_dict['dihedral'+add_text] = int_ge_zero(dihedrals[index])
#                 moltype_dict['improper'+add_text] = int_ge_zero(impropers[index])
#             self._moltype_dict = moltype_dict
#
#         except (ValueError, IndexError):
#             raise AssertionError("Unexpected value for %s!" % self.__class__.__name__)
#
#     def __str__(self):
#         out = ''
#         for key, value in self._moltype_dict.items():
#                 out += str(value) + ' ' + key + '\n'
#         return out


# ==========================================================================================


# if __name__ == '__main__':

    # atom1 = Atom(atom_id=1, molecule_id=1, atom_type=1, q=0, x=0.3, y=0, z=0, imx=0, imy=0, imz=0, label='')
    # print (atom1)
    #
    # box1 = Box(xlo=1, xhi=2, ylo=-1, yhi=2.3, zlo=92, zhi=23)
    # print (box1)

    # bond1 = Bond(bond_id=1, bond_type=1, aid_i=1, aid_j=2)
    # print (bond1)
    #
    # angle1 = Angle(angle_id=1, angle_type=1, aid_i=2, aid_j=4, aid_k=5, label=' # water angle')
    # print (angle1)
    #
    # dihedral1 = Dihedral(dihedral_id=1, dihedral_type=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    # print (dihedral1)
    #
    # improper1 = Improper(improper_id=1, improper_type=1, aid_i=1, aid_j=2, aid_k=3, aid_l=4)
    # print (improper1)
    #
    # mass1 = Mass(mass_id=1, mass=2.3, label='O')
    # print (mass1)
    #
    # moltype1 = MolType(atoms=[100, 2], bonds=[21, 1])
    # print (moltype1)