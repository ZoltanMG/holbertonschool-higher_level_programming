#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ My subclass """

    def print_sorted(self):
        """ Print sorted """

        new_list = MyList()
        for i in self:
            new_list.append(i)
        print(sorted(new_list))
