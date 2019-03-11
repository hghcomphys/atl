
import pytest
from .atom import Atom
from .molsection import AtomsSection


def test_atom():
    """Test Atom"""

    # make Atom instance
    atom = Atom(atom_id=1, molecule_id=1, atom_type=1, q=+0.1, x=0.3, y=0.4, z=0.7, imx=0, imy=0, imz=0, label='Cu')

    # atom properties
    assert isinstance(atom, Atom)
    assert atom.x == 0.3
    assert atom.y == 0.4
    assert atom.z == 0.7
    assert atom.label == 'Cu'

    # exceptions
    with pytest.raises(TypeError):
        Atom()
    with pytest.raises(AssertionError):
        Atom(atom_id='a', molecule_id=1, atom_type=1, q=+0.1, x=0.3, y=0.4, z=0.7)


def test_atom_section():
    """Test AtomSection"""

    # make atom instances
    atom1 = Atom(atom_id=1, molecule_id=1, atom_type=1, q=+0.1, x=0.3, y=0.4, z=0.7, imx=0, imy=0, imz=0, label='Cu')
    atom2 = Atom(atom_id=2, molecule_id=2, atom_type=2, q=-0.1, x=0.5, y=0.6, z=0.8, imx=1, imy=1, imz=1, label='Fe')

    # test with no argument
    atoms_section = AtomsSection()
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.name == 'Atoms'

    # one atom
    atoms_section.add(atom1)
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.get_atoms_number() == 1
    assert atoms_section.atoms[0].label == 'Cu'
    assert atom1 in atoms_section.items

    # one atom (another method)
    atoms_section = AtomsSection(atom1)
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.get_atoms_number() == 1
    assert atoms_section.atoms[0].label == 'Cu'
    assert atom1 in atoms_section.items

    # two atoms
    atoms_section = AtomsSection([atom1, atom2])
    assert isinstance(atoms_section, AtomsSection)
    assert atoms_section.get_atoms_number() == 2
    assert atoms_section.atoms[0].label == 'Cu'
    assert atoms_section.atoms[1].label == 'Fe'

    # assign (=) operator
    atoms_section = AtomsSection(atom1)
    new_atoms_section = atoms_section
    assert isinstance(new_atoms_section, AtomsSection)
    assert new_atoms_section.get_atoms_number() == atoms_section.get_atoms_number()
    assert new_atoms_section.atoms[0].label == atoms_section.atoms[0].label

    # integration (+) operator
    atoms_section1 = AtomsSection(atom1)
    atoms_section2 = AtomsSection(atom2)
    new_atoms_section = atoms_section1 + atoms_section2
    assert isinstance(new_atoms_section, AtomsSection)
    assert new_atoms_section.get_atoms_number() == (atoms_section1.get_atoms_number()+atoms_section2.get_atoms_number())
    assert atom1.label == new_atoms_section.atoms[0].label
    assert atom2.label == new_atoms_section.atoms[1].label

    with pytest.raises(AssertionError):
        AtomsSection(1)

    with pytest.raises(AssertionError):
        AtomsSection([1, 2])

