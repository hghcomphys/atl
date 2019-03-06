"""
handling input/output methods in molecular frame
"""

from abc import abstractmethod


class Formatter:

    def __init__(self, molecular_frame):
        self.molecular_frame = molecular_frame

    # static method, this is implicitly a class method
    def make(self, format):
        try:
            # subclass name has to start with "Formatter"!
            formatter = eval("Formatter"+str(format))(self.molecular_frame)

        except (SyntaxError, NameError, TypeError):
            raise AssertionError("Unexpected type for Formatter!")
        return formatter


class FormatterXYZ(Formatter):

    def write(self, file_name):
        with open(file_name, "w") as fp:
            atoms_section = self.molecular_frame.sections['Atoms']
            fp.write('%d\n\n'%atoms_section.get_atoms_number())
            for atom in atoms_section.get_list():
                fp.write("%s %f %f %f\n"%(atom.label, atom.x, atom.y, atom.z))