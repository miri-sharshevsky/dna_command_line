from commands.batch.batch import Batch


class Listening_batches_command(Batch):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Listening_batches_command.__instance:
            Listening_batches_command.__instance = object.__new__(cls)
        return Listening_batches_command.__instance

    def run_command(self, command):
        """
        Shows a list of all the batch names.
        Required command: batchlist
        """
        if command != "batchlist":
            return "in valid batchlist arguments"
        return " ".join(super().get_batch_holder().get_batches_name())
