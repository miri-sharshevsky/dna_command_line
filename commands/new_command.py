from commands.command import Command
from commands.parser import Parser


class New_command(Parser):

    __instance = None


    def __new__(cls, *args, **kwargs):
        if not New_command.__instance:
            New_command.__instance = object.__new__(cls)
        return New_command.__instance

    def run_command(self, command):
        """
        Creates a new sequence, as described by the followed sequence.
        If the @<sequence_name> is used, then this will be the name of the new sequence.
        Otherwise, a default name will be provided
        :param command: New command to run
        :return: The result printed
        """
        # command = command.split(" ")
        # if not 2 <= len(command) <= 3 or (len(command) > 2 and not command[2].startswith('@')):
        #     return "iv valid command"
        command = super().run_command(command)
        if len(command) > 3:
            return "in valid command"
        try:
            return super().get_dna_holder().add_dna(command[0], command[1])
        except:
            return command
