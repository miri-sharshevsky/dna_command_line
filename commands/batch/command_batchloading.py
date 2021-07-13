import os

from commands.batch.batch import Batch


class Batchload(Batch):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Batchload.__instance:
            Batchload.__instance = object.__new__(cls)
        return Batchload.__instance

    def run_command(self, command):
        """
        Loading a batch is done using the command batchload, followed by the filename to
            be loaded
        Required command: batchload [file_name] : <@batch_name>
        """
        command = command.split(" ")
        if not 2 <= len(command) <= 3:
            return "In valid batchload arguments"
        name = (os.path.splitext(os.path.basename(command[1])))[0] if len(command) == 2 else command[2][1:]
        try:
            with open(command[1], 'r') as file:
                batch = file.readlines()
                for i in range(len(batch)):
                    batch[i] = batch[i].replace('\n', '')
                super().get_batch_holder().add_batch(name, batch)
        except Exception:
            return "In valid file path"
