#!/usr/bin/python3
""" command interpreter """
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """ class definition of the command interpreter """
    
    __classNames = ["BaseModel",]

    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance, saves it
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
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        arg = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
            return

        if arg[0] not in self.__classNames:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("* instance id missing **")
        else:
            instance_name = arg[0]
            instance_id = arg[1]
            key = "{}.{}".format(instance_name, instance_id)
            obj = storage.all()

            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

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
