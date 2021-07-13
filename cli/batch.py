from cli.cli import CLI
from data_base.batches_holder import Batch_holder


class Batch(CLI):
    def __init__(self, batch_name):
        super().__init__("> batch >>>")
        self.__is_running = True
        self.__batch_name = batch_name
        self.__batch_holder = Batch_holder()

    def get_batch_holder(self):
        return self.__batch_holder


    def run_command(self):
        commands = []
        while self.__is_running:
            command = input(super().get_prompt())
            if command == "end":
                self.__is_running = False
            else:
                commands.append(command)
        self.__batch_holder.add_batch(self.__batch_name, commands)