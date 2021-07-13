from cli.cli import CLI
from commands.batch.command_run_batch import Run_batch_Command
from commands.invoker import Invoker


class CMD(CLI):
    def __init__(self):
        super().__init__("> cmd >>>")
        self.__invoker = Invoker()

    def get_invoker(self):
        return self.__invoker

    def run_command(self):
        while True:
            command = input(super().get_prompt())
            if command.startswith("run"):
                self.__invoker.get_factory().set_commands_dictionary("run", Run_batch_Command())
            value = self.__invoker.run_command(command)
            if value == "Command_Stopped":
                print("Thank you for using Dnalanyzer.\nGoodbye!!")
                return
            if value is not None:
                print(value)


