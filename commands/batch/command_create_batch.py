import cli
from commands.command import Command


class Create_batch(Command):
    __instance = None
    __batch = None

    def __new__(cls, *args, **kwargs):
        if not Create_batch.__instance:
            Create_batch.__instance = object.__new__(cls)
        return Create_batch.__instance

    def run_command(self, command):
        """
        Creating a new batch and wating for the user to insert the new batch's commands
        Required command: batch <batch_name>
        Ending with inserting the command end
        """
        command = command.split(" ")
        if len(command) != 2:
            return "in valid batch command arguments"
        self.__batch = cli.Batch(command[1])
        self.__batch.run_command()

