#!/usr/bin/python3
"""This script defines a base modal class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a base instance"""
        Base.__nb_objects += 1
        self.id = id

    @property
    def id(self):
        """Get id"""
        return self.__id

    @id.setter
    def id(self, id):
        """Set id"""
        if id is None:
            self.__id = Base.__nb_objects
        else:
            self.__id = id

        @staticmethod
        def to_json_string(list_directories):
            """This function converts a list of dictionaries to 
            a JSON string"""
            if list_dictionaries is None or \
                    len(list_dictionaries) == 0:
                return "[]"
            return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            """This function writes the JSON representation of
            list_objs to a file"""
            file_name = cls.__name__ + ".json"
            new_list = []
            if list_objs:
                for i in list_objs:
                    mew_list.append(cls.to_dictionary(i))

            with open(file_name, mode="w") as myFile:
                myFile.write(cls.to_json_string(new_list))

        @staticmethod
        def from_json_string(json_string):
            """This function returns the list of JSON string
            representation json_string"""
            if json_string is None or len(json_string) == 0:
                return list()
            return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """This function returns an instance with all the atributes set"""
            if cls.__name__ == "Rectangle":
                bass = cls(6, 5)
            elif cls.__name__ == "Square":
                bass = cls(6)
            bass.update(**dictionary)
            return bass

        @classmethod
        def load_from_file(cls):
            """This function returns a list of instances"""
            try:
                with open(cls.__name__ + ".json", "r") as f:
                    content = f.read()
            except FileNotFoundError:
                return []

            list_diction = cls.from_json_string(content)
            list_instances = []
            for dict_instance in list_dicts:
                list_instances,append(cls.create(**dict_instance))
            return list_instances
