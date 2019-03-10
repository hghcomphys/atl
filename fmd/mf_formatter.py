"""
handling input/output methods in molecular frame
"""

from mf_atom import AtomsSection


class Formatter:

    def __init__(self, molecular_frame):
        self._molecular_frame = molecular_frame

    # static method, this is implicitly a class method
    def make(self, format):
        try:
            # subclass name has to start with "Formatter"!
            formatter = eval("Formatter"+str(format))(self._molecular_frame)

        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected type for Formatter!")
        return formatter


class FormatterXYZ(Formatter):

    def write(self, file_name):
        with open(file_name, "w") as out_file:
            atoms_section = self._molecular_frame.get_molecular_section('Atoms')
            out_file.write('%d\n\n'%atoms_section.get_atoms_number())
            for atom in atoms_section.get_atoms():
                out_file.write("%s %f %f %f\n"%(atom.label, atom.x, atom.y, atom.z))

    def read(self, file_name, frame=-1):
        """
        This function reads specific frame of a *.xyz file and returns molecular frame
        """
        n_frame = 0  # initializing frame counter to zero
        atoms = []  # list of readed frames
        with open(file_name, 'r') as in_file:

            # loop over lines in file
            for line in in_file:

                n_atoms = int(line)  # read number of atoms at the begging of the frame
                next(in_file)  # skip one line
                n_frame += 1  # increment frame
                if n_frame >= frame:
                    for index in range(n_atoms):
                        line = next(in_file)
                        line = line.rstrip("/n").split()
                        atom = Atom(atom_id=index+1, molecule_id=0, atom_type=0, q=0.0, x=float(line[1]),
                                    y=float(line[2]), z=float(line[3]), label=line[0])
                        atoms.append(atom)
                else:
                    # skipping the frame
                    for i in range(n_atoms):
                        next(in_file)

                # check either desired frame or last frame is reached
                if (frame > 0) and (n_frame >= frame):
                    break

        atom_section = AtomsSection()
        atom_section.add_atoms(atoms)
        self._molecular_frame.set_molecular_section(atom_section)

        # returning molecular section
        return self._molecular_frame.get_molecular_sections()


