from commands import Command
from data_base import Batch_holder


class Showing_batch(Command):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Showing_batch.__instance:
            Showing_batch.__instance = object.__new__(cls)
        return Showing_batch.__instance

    def run_command(self, command):
        """
        Showes the command of the given batch name
        Required command:  batchshow <@batch_name>
        """
        command = command.split(" ")
        if len(command) != 2 or not command[1].startswith('@'):
            return "in valid batchshow arguments"
        batch_holder = Batch_holder()
        try:
            return " | ".join(batch_holder.get_batch_by_name(command[1][1:]))
        except Exception as error:
            return error
