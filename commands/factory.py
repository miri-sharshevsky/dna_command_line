import commands
from commands.analysis.command_len import Len


class Factory:
    """
    Factory for handling all the command
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Factory.__instance:
            Factory.__instance = object.__new__(cls)
        return Factory.__instance

    def __init__(self):
        self.__commands_dictionary = {"new": commands.New_command(),
                                      "load": commands.Load_command(),
                                      "dup": commands.Dup_command(),
                                      "slice": commands.Slice(),
                                      "replace": commands.Replace(),
                                      "rename": commands.Rename(),
                                      "del": commands.Del(),
                                      "save": commands.Save(),
                                      "len": Len(),
                                      "find": commands.Find(),
                                      "count": commands.Count(),
                                      "findall": commands.Find_all(),
                                      "batch": commands.Create_batch(),
                                      "batchlist": commands.Listening_batches_command(),
                                      "batchshow": commands.Showing_batch(),
                                      "batchsave": commands.Saving_batch(),
                                      "batchload": commands.Batchload(),
                                      "list": commands.List(),
                                      "quit": commands.Quit()
                                      }

    def get_command(self, command_name):
        """
        Get the command by the command_name
        """
        try:
            return self.__commands_dictionary[command_name]
        except:
            raise ValueError

    def set_commands_dictionary(self, new_command_name, command_class):
        self.__commands_dictionary[new_command_name] = command_class
