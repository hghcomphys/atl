
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

    # atom errors
    with pytest.raises(TypeError):
        Atom()
    with pytest.raises(AssertionError):
        Atom(atom_id='a', molecule_id=1, atom_type=1, q=+0.1, x=0.3, y=0.4, z=0.7)


def test_atom_section():
    """Test AtomSection"""

    # make Atom instances
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

    # one atom
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

