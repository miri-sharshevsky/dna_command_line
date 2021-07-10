from cli.cli import CLI
from invoker import Invoker



class CMD(CLI):
    def __init__(self):
        super().__init__("> cmd >>>")
        self.__invoker = Invoker()

    def get_invoker(self):
        return self.__invoker

    def run(self):
        while True:
            command = input(super().get_prompt())
            value = self.__invoker.run_command(command)
            if value:
                print(value)


