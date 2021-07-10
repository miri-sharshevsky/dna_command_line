from commands.management.dell import Dell
from commands.management.rename import Rename
from commands.management.save import Save
from commands.new_command import New_command
from commands.load_command import Load_command
from commands.dup_command import Dup_command
from commands.manipulation.replace import Replace
from commands.manipulation.slice import Slice


class Factory:
    """
    Factory for handling all the command
    """
    def __init__(self):
        self.__commands_dictionary = {"new": New_command(),
                                      "load": Load_command(),
                                      "dup": Dup_command(),
                                      "slice": Slice(),
                                      "replace": Replace(),
                                      "rename": Rename(),
                                      "dell": Dell(),
                                      "save": Save()
                                      }

    def get_command(self, command_name):
        try:
            return self.__commands_dictionary[command_name]
        except:
            raise ValueError

