"""
Calculate Lennard-jones cross-atom parameters
"""
import math


def intermol_lj_param(mol1, mol2, ignore_self_interact=False):
    """
    This function generates the inter-molecular LJ parameters based on
    combination rules of sqrt(e1,e2) and (s1+s2)/2.
    Two input arguments are molecules each in form of dictionary.

    Example:

        methanol={
        'C(CH3)':[12, 6.630154972997068241E-02, 3.581179283634555510E+00],
        'O(OH)':[3, 2.030610329881481768E-01, 2.954841833242532800E+00],
        'H(CH3)': [20, 2.829367882355780447E-02, 2.373408142809749322E+00],
        'H(OH)':[21, 0.000000000000000000E+00, 0.000000000000000000E+00]
        }

        water={
            'Ow':[68,  0.15530000,  3.166],
            'Hw':[69,  0.00000000,  0.000]
        }

        intermol_lj_param(water,methanol)
    """

    def eps(e1, e2):
        return math.sqrt(e1 * e2)

    def sig(s1, s2):
        return (s1 + s2) * 0.5

    print('# Generated by ATL "intermol_lj_param()"')
    for mol in [mol1, mol2]:
        for m in mol.keys():
            if not ignore_self_interact:
                print('pair_coeff %5d %5d %1.10f %1.10f # %s-%s' % (mol[m][0], mol[m][0],
                                                                 mol[m][1], mol[m][2], m, m))
            # print '# -------- '

    for m1 in mol1.keys():
        for m2 in mol2.keys():

            if mol1[m1][0] < mol2[m2][0]:
                print('pair_coeff %5d %5d %1.10f %1.10f # %s-%s' % (mol1[m1][0], mol2[m2][0],
                                                                    eps(mol1[m1][1], mol2[m2][1]),
                                                                    sig(mol1[m1][2], mol2[m2][2]),
                                                                    m1, m2))
            elif mol1[m1][0] > mol2[m2][0]:
                print('pair_coeff %5d %5d %1.10f %1.10f # %s-%s' % (mol2[m2][0], mol1[m1][0],
                                                                    eps(mol1[m1][1], mol2[m2][1]),
                                                                    sig(mol1[m1][2], mol2[m2][2]),
                                                                    m1, m2))
            else:
                print('Warning: two mols have the same atom type!!!')
                print('pair_coeff %5d %5d %1.10f %1.10f # %s-%s' % (mol2[m2][0], mol1[m1][0],
                                                                    eps(mol1[m1][1], mol2[m2][1]),
                                                                    sig(mol1[m1][2], mol2[m2][2]),
                                                                    m1, m2))
    return
