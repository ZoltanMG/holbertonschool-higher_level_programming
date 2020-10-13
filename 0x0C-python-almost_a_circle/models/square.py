#!/usr/bin/python3
""" class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ init """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """

        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size_(self):
        """ getter """

        return self.width

    @size.setter
    def size(self, value):
        """ setter """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """

        if args:
            arguments = ['id', 'size', 'x', 'y']
            for idx, value in enumerate(args):
                setattr(self, arguments[idx], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ to dictionary """

        dictionary = {"id": self.id,
                      "size": self.ize,
                      "x": self.x,
                      "y": self.y}
        return dictionary
