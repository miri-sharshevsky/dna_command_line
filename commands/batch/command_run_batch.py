import data_base
from commands import Batch
from commands.command import Command
from commands.invoker import Invoker


class Run_batch_Command(Batch):
    __instance = None
    __invoker = Invoker()

    def __new__(cls, *args, **kwargs):
        if not Run_batch_Command.__instance:
            Run_batch_Command.__instance = object.__new__(cls)
        return Run_batch_Command.__instance

    def run_command(self, command):
        """
         runs a batch, that is, executes it as if the commands were entered manually
        Required command:  run <@batchname>
        """
        command = command.split(" ")
        if len(command) != 2:
            return "In valid run batch arguments"
        try:
            commands = super().get_batch_holder().get_batch_by_name(command[1][1:])
        except Exception as error:
            return error
        res = []
        for command in commands:
            try:
                res.append(str(self.__invoker.run_command(command)))
            except Exception as error:
                res.append(str(error))

        return "\n".join(res)

