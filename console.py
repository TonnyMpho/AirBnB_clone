#!/usr/bin/python3
""" command interpreter """
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """ class definition of the command interpreter """

    __classNames = ["BaseModel"]

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance, saves it
        (to the JSON file) and prints the id
        """
        if arg:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        arg = arg.split()

        if not self.validate_args(arg, self.__classNames):
            return
        else:
            instance_name = arg[0]
            instance_id = arg[1]
            key = "{}.{}".format(instance_name, instance_id)
            obj = storage.all()

            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()

        if not self.validate_args(args, self.__classNames):
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all()

        if key in obj:
            del obj[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        instances = storage.all()

        if arg:
            objects = []
            if arg not in self.__classNames:
                print("* class doesn't exist **")
            else:
                for key, instance in instances.items():
                    if key.startswith(arg):
                        objects.append(str(instance))
                print(objects)

        else:
            objects = []
            for instance in instances.values():
                objects.append(str(instance))
            print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> <attribute value>"""
        args = arg.split()

        if not self.validate_args(args, self.__classNames):
            return

        instances = storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key not in instances.keys():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            return

        instance = instances[key]
        setattr(instance, args[2], args[3])
        instance.save()

    def validate_args(self, args, cls_names):
        """ Check if arguments were passed """
        if len(args) < 1:
            print("** class name missing **")
            return False

        if args[0] not in cls_names:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("* instance id missing **")
            return False

        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF - End of file to exit the program """
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
