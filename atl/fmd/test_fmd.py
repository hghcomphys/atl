"""FMD package tests"""


import pytest
from .atom import Atom
from .molsection import AtomsSection
from .molframe import MolecularFrame

import numpy as np
from ase.build import bulk
from ase.build.supercells import make_supercell

# ======================================= Atom

# @pytest.fixture
def atom1():
    return Atom(atom_id=1, molecule_id=1, atom_type=1, q=+0.1, x=0.3, y=0.4, z=0.7, imx=0, imy=0, imz=0, label='Cu')


# @pytest.fixture
def atom2():
    return Atom(atom_id=2, molecule_id=2, atom_type=2, q=-0.1, x=0.5, y=0.6, z=0.8, imx=1, imy=1, imz=1, label='Fe')


def test_atom():
    assert isinstance(atom1(), Atom)
    assert atom1().x == 0.3
    assert atom1().y == 0.4
    assert atom1().z == 0.7
    assert atom1().label == 'Cu'


def test_atom_exceptions():

    with pytest.raises(TypeError):
        Atom()

    with pytest.raises(AssertionError):
        Atom(atom_id='a', molecule_id=1, atom_type=1, q=+0.1, x=0.3, y=0.4, z=0.7, label='Ge')

# ======================================= Atoms Section


def test_atoms_section():
    atoms_section = AtomsSection()
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.name == 'Atoms'


def test_atoms_section_add():
    atoms_section = AtomsSection()
    atoms_section.add(atom1())
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.get_atoms_number() == 1
    assert atoms_section.atoms[0].label == atom1().label


def test_atoms_section_constructor():
    atoms_section = AtomsSection(atom1())
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.get_atoms_number() == 1
    assert atoms_section.atoms[0].label == atom1().label


def test_atoms_section_list():
    atoms_section = AtomsSection([atom1(), atom2()])
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.get_atoms_number() == 2
    assert atoms_section.atoms[0].label == atom1().label
    assert atoms_section.atoms[1].label == atom2().label


def test_atoms_section_equal():
    atoms_section = AtomsSection(atom1())
    new_atoms_section = atoms_section
    assert isinstance(new_atoms_section, AtomsSection)
    assert new_atoms_section.get_atoms_number() == atoms_section.get_atoms_number()
    assert new_atoms_section.atoms[0].label == atoms_section.atoms[0].label


def test_atoms_section_plus():
    atoms_section1 = AtomsSection(atom1())
    atoms_section2 = AtomsSection(atom2())
    new_atoms_section = atoms_section1 + atoms_section2
    assert isinstance(new_atoms_section, AtomsSection)
    assert new_atoms_section.get_atoms_number() == (atoms_section1.get_atoms_number()+atoms_section2.get_atoms_number())
    assert atom1().label == new_atoms_section.atoms[0].label
    assert atom2().label == new_atoms_section.atoms[1].label


def test_atoms_section_exceptions():

    with pytest.raises(AssertionError):
        AtomsSection(1)

    with pytest.raises(AssertionError):
        AtomsSection([1, 2])

# ======================================= Molecular Frame

def make_supercell_cu():
    crys = bulk('Cu', 'fcc', a=3.6, orthorhombic=True)
    P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * 5
    return make_supercell(crys, P)


def make_supercell_li():
    crys = bulk('Li', 'bcc', a=3.51, orthorhombic=True)
    P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * 10
    return make_supercell(crys, P)


def test_molecular_frame():
    mf = MolecularFrame()
    assert isinstance(mf, MolecularFrame)
    assert mf.name == 'Molecular Frame'


def test_molecular_frame_import_ase():
    mf = MolecularFrame('Cu crystal')
    mf.import_from(package_instance=make_supercell_cu(), package_name="ASE")
    assert mf.get_atoms_number() == make_supercell_cu().get_number_of_atoms()
    assert mf.name == 'Cu crystal'
    assert pytest.approx(mf.get_atoms()[1].x) == make_supercell_cu().get_positions()[1][0]  # second atom x position
    assert mf.get_atoms()[1].label == 'Cu'  # second atom label


def test_molecular_frame_equal():
    mf = MolecularFrame('Cu crystal').import_from(make_supercell_cu())
    new_mf = mf  # equal operator
    assert new_mf.get_atoms_number() == mf.get_atoms_number()
    assert new_mf.name == mf.name
    assert new_mf.get_atoms()[1].x == mf.get_atoms()[1].x  # atom x position
    assert new_mf.get_atoms()[1].label == mf.get_atoms()[1].label # second atom label
    # TODO: limited to atoms section!


def test_molecular_frame_plus():
    mf1 = MolecularFrame('Cu crystal').import_from(make_supercell_cu())
    mf2 = MolecularFrame('Li crystal').import_from(make_supercell_li())
    mf = mf1 + mf2 # plus operator
    assert isinstance(mf, MolecularFrame)
    assert mf1.name in mf.name and mf2.name in mf.name
    assert mf.get_atoms_number() == mf1.get_atoms_number() + mf2.get_atoms_number()
    # TODO: limited to atoms section!


def test_molecular_frame_select_region():

    def sphere(x, y, z):
        """sphere region"""
        if np.sqrt(x**2+y**2+z**2)<7.0:
            return True
        else:
            return False

    mf = MolecularFrame('Li crystal').import_from(make_supercell_li())
    sel_mf = mf.select_atoms_region(region_fn=sphere)
    assert isinstance(sel_mf, MolecularFrame)
    assert sel_mf.get_atoms_number() == 12
    # TODO: limited to atom sections
