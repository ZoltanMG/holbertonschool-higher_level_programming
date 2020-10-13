#!/usr/bin/python3
""" base class"""


import json


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file """

        filename = cls.__name__ + '.json'
        list_instances = []
        if list_objs is not None:
            for instance in list_objs:
                list_instances.append(instance.to_dictionary())

        with open(filename, 'w', encoding='utf-8') as a_file:
            a_file.write(cls.to_json_string(list_instances))

    def from_json_string(json_string):
        """ from_json_string """

        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ create """

        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)

        dummy.update(**dictionary)
        return dummy
