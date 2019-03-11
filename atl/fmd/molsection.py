"""Defining molecular sections"""

from copy import deepcopy


class MolecularSection:
    """Defining base class for each molecular frame section such as AtomSection."""
    def __init__(self, name):
        self.__name = str(name)  # setting molecular section name
        self.__items = []  # empty list of items

    @property
    def name(self):
        """This method returns given name of molecular section."""
        return self.__name

    @property
    def items(self):
        """This method returns list of items within molecular section."""
        return self.__items

    def add(self, item):
        """This method adds an item to molecular section."""
        self.__items.append(item)
        return self

    def add_items(self, items):
        """This methods adds a list of items to molecular section."""
        for item in items:
            self.add(items)
        return self

    def get_items_number(self):
        """This method returns number of items within the molecular section."""
        return len(self.items)

    def __str__(self):
        """This method defines string conversion of a molecular section instance."""
        out = self.name + "\n\n"
        for item in self.items:
            out += str(item) + '\n'
        return out

    def __eq__(self, other):
        """This method defines equal '=' operator between two molecular section instances."""
        if not isinstance(other, MolecularSection):
            AssertionError("Expected %s for '=' operator!" % self.__class__.__name__)
        # set name and items
        self.__name = other.name
        self.__items = deepcopy(other.items)
        return self
