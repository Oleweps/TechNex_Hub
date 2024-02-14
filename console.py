#!/usr/bin/python3
""" Console for DLA Instrumentation Hub """

import cmd
from models import storage
from datetime import datetime
import shlex

classes = ["User", "ServiceRequest", "Service", "EquipmentListing",
           "Message", "AuthenticationToken", "Feedback", "Suggestion",
           "Admin", "Notification"]


class TekHubConsole(cmd.Cmd):
    """ Console class for DLA Instrumentation Hub """
    prompt = '(tek_hub) '

    def emptyline(self):
        """ Do nothing on empty line (just pressing Enter) """
        pass

    def do_EOF(self, arg):
        """ Exits console when EOF is received (Ctrl + D) """
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_create(self, arg):
        """ Create a new instance of a class """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = storage.create_instance(args[0], args[1:])
        print(new_instance.id)
        storage.save()

    def do_show(self, arg):
        """ Print an instance based on the class name and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance = storage.get(args[0], args[1])
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete an instance based on the class name and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance = storage.get(args[0], args[1])
        if instance:
            storage.delete(instance)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Print string representations of instances """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in classes:
            obj_dict = storage.all(args[0])
        else:
            print("** class doesn't exist **")
            return
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """ Update an instance based on the class name, id, attribute & value """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance = storage.get(args[0], args[1])
        if instance:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(instance, args[2], args[3])
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    TekHubConsole().cmdloop()
