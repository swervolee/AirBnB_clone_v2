#!/usr/bin/python3
"""
A console for the Hbnb
"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Hbnb commandline"""

    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

    class_list = {"BaseModel": BaseModel, "User": User,
                  "Place": Place, "State": State,
                  "City": City, "Amenity": Amenity,
                  "Review": Review}
    dots = ["all", "count", "show", "destroy", "update"]

    def do_EOF(self, signal):
        """
        Exits the program upon EOF signal which is ctrl + d
        """
        print("")
        return True

    def preloop(self):
        """
        Prints the prompt only if isatty is false
        """
        if not sys.__stdin__.isatty():
            print("(hbnb)")

    def do_quit(self, cmd):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Does nothing to an empty line command
        """
        pass

    def do_create(self, args=None):
        """
        Creates a new instance of BaseModel saves it
        to json file and prints out the id of the instance
        """
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kw = {}
            for arg in arg_list[1:]:
                arg_splited = arg.split("=")
                arg_splited[1] = eval(arg_splited[1])
                if type(arg_splited[1]) is str:
                    arg_splited[1] = arg_splited[1].replace("_", " ").replace('"', '\\"')
                kw[arg_splited[0]] = arg_splited[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        new_instance = HBNBCommand.class_list[arg_list[0]](**kw)
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """
        Help information for the create command
        """
        print("Creates a new instance")
        print("[Usage]: create <className>")

    def do_show(self, cmd=None):
        """
        Prints the string representation of an instance
        given the class name and the instance id
        Prints a list of strings
        """
        name, id = None, None
        dc = storage.all()

        if cmd:
            cmd_list = cmd.split(" ")  # Store the commands in a list
            if len(cmd_list) >= 1:
                name = cmd_list[0]

            if len(cmd_list) >= 2:
                id = cmd_list[1]
        if not cmd:
            print("** class name missing **")

        elif not name or name not in self.class_list:
            print("** class doesn't exist **")

        elif not id:
            print("** instance id missing **")

        elif f"{name}.{id}" not in dc:
            print("** no instance found **")

        else:
            print(dc[f"{name}.{id}"])

    def help_show(self):
        """
        Help info for the show command
        """
        print("Displays a single instance")
        print("[Usage]: show <ClassName> <Id>\n")

    def do_destroy(self, cmd=None):
        """
        Destroys an instance based on class name and
        instance id
        """

        name, id = None, None
        all_objects = storage.all()
        if cmd:
            cmd_list = cmd.split(" ")
            if len(cmd_list) >= 1:
                name = cmd_list[0]
            if len(cmd_list) >= 2:
                id = cmd_list[1]

        if not name:
            print("** class name missing **")
        elif not id:
            print("** instance id missing **")
        elif name not in self.class_list:
            print("** class doesn't exist **")
        elif f"{name}.{id}" not in all_objects:
            print("** no instance found **")
        else:
            all_objects.pop(f"{name}.{id}")
            storage.save()

    def help_destroy(self):
        """
        help info for the destroy command
        """
        print("Destroys a class instance")
        print("[usage] destroy <className> <ObjectId>\n")

    def do_all(self, arg=None):
        """
        Prints all instances of the class name is absent
        else prints all the instances of the given class
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.class_list.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.class_list.get(arg)])

    def help_all(self):
        """
        Help for the all command
        """
        print("Prints all object instances of a command")
        print("[usage]: all <ClassName>\n")

    def do_update(self, cmd=None):
        """
        Updates a class with new attributes
        or new values
        command syntax: update <clsname> <id> <attrName> <attrValue>
        """
        cls_name, id, attr_name, attr_val = None, None, None, None
        all_objects = storage.all()

        arg_tuple = cmd.partition(" ")  # Extract the clsName
        if arg_tuple[0]:
            cls_name = arg_tuple[0]
        else:
            print("** class name missing **")
            return

        if cls_name not in self.class_list:
            print("** class doesn't exist **")
            return

        arg_tuple = arg_tuple[2].partition(" ")  # Skip clsName and " "
        if arg_tuple[0]:
            id = arg_tuple[0]  # (<id>, " ", <arguments>)
        else:
            print("** instance id missing **")
            return

        key = f"{cls_name}.{id}"  # Key of storage.all() <clsname.id>

        if key not in storage.all():
            print("** no instance found **")
            return
        item_dict = all_objects[key]  # Key the object

        if '{' in arg_tuple[2] and '}' in arg_tuple[2] and\
           type(eval(arg_tuple[2])) is dict:
            cmd_list = []  # If args is dict, list it, [key, value]
            for k, v in eval(arg_tuple[2]).items():
                cmd_list.append(k)
                cmd_list.append(v)
        else:
            arg = arg_tuple[2]
            arg = arg.strip()
            if arg and arg.startswith("\""):  # # Else check for <">
                attr_name = arg[1:arg.find("\"", 1)]  # Extract btwn ""
                arg = arg[arg.find("\"", 1) + 1:]  # Move the cursor frwd
            arg = arg.partition(" ")  # Else partition again

            if not attr_name and arg[0] != " ":  # if no quotations
                attr_name = arg[0]
            if arg[2] and arg[2][0] == "\"":
                attr_val = arg[2][1: arg[2].find("\"", 1)]
            if arg[2] and not attr_val:
                attr_val = arg[2].partition(" ")[0]
            cmd_list = [attr_name, attr_val]
        for i in range(len(cmd_list)):
            if i % 2 == 0:  # Parse the commands in two's [Key, Value]
                attr_name, attr_value = cmd_list[i], cmd_list[i + 1]
                if not attr_name:
                    print("** attribute name missing **")
                    return
                if not attr_value:
                    print("** value missing **")
                    return
                if hasattr(eval(cls_name)(), attr_name):  # If attr exists
                    attr_value = type(getattr(eval(cls_name),  # cast val
                                              attr_name))(attr_value)
                setattr(item_dict, attr_name, attr_value)
                item_dict.save()  # Save the changes to file.json

    def help_update(self):
        """
        Help information for updating class
        """
        print("Updates a class intance with new information")
        print("[usage]: update <ClassName> <Id> <AtrrName> <AttrValue>\n")

    def do_count(self, cmd):
        """
        counts the number of instances of a class
        """
        all_objects = storage.all()
        count = 0

        for k in all_objects:
            if cmd in k:
                count += 1
        print(count)

    def default(self, cmd):
        """
        Handles class commands
        Class commands syntax is:
            <ClsName>.<Commmand><(Arguments)>
        if the command syntax is wrong print
        error message
        """
        line = cmd[:]  # copy the command
        if not("." in line and "(" in line and ")" in line):
            print(f"*** Unknown syntax: {cmd}")  # <ClsName>.<Command>(Args)
            return
        cls_name = line[: line.find(".", 1)]  # extract the cls name
        if cls_name not in self.class_list:  # Look it up in the clslist
            print(f"*** Unknown syntax: {line}")
            return
        comd = line[line.find(".", 1) + 1: line.find("(", 1)]  # Eg update, all
        if comd not in self.dots:
            print(f"*** Unknown syntax: {line}")
            return
        if comd == "all":  # prints all the classes in file.json
            self.do_all(cls_name)
        if comd == "count":  # Count the number of instances of a class
            self.do_count(cls_name)
        if comd == "show":  # prints a string representation of a cls
            id = line[line.find("(", 1) + 1: line.find(")", 1)]
            joined_command = " ".join([cls_name, id])
            self.do_show(joined_command)
        if comd == "destroy":  # Destroys an instance
            id = line[line.find("(", 1) + 1: line.find(")", 1)]
            joined_command = " ".join([cls_name, id])
            self.do_destroy(joined_command)
        if comd == "update":  # Updates an isntance with new attrs/values
            arg = line[line.find("(", 1) + 1: line.find(")", 1)]  # Extract
            arg = arg.partition(", ")  # The args are comma seperated so ..
            id = arg[0]  # Extract the id which is the first args
            cmd2 = arg[2]  # Jump id and " ".Extracts args after id
            cmd2 = cmd2.strip()  # Eliminate trailing whitespaces
            if cmd2 and cmd2[0] == "{" and cmd2[-1] == "}"\
               and type(eval(cmd2)) is dict:
                attrs = cmd2  # If its a dict, take it as it is
            else:
                attrs = cmd2.replace(",", "")  # Else eliminate commas
            joined = " ".join([cls_name, id, attrs])  # Join the commands
            self.do_update(joined)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
