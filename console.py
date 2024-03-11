#!/usr/bin/python3
"""
Contains entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter for HBNB project
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Handles EOF signal (Ctrl+D) to exit the program
        """
        print("")  # New line for better output formatting
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Creates new instance of BaseModel, saves it and prints the id
        Usuage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        new_instance = storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints string repr of all instances based or not on class name
        Usage: all [<class name>]
        """
        args = arg.split()
        obj_list = []
        if not arg:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
