from commands.command import Command
from data_base import Batch_holder


class Batch(Command):
    """
    Class for all the batch commands
    """
    __batch_holder = Batch_holder()

    def get_batch_holder(self):
        return self.__batch_holder