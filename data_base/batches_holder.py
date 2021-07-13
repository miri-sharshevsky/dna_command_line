class Batch_holder:
    """
    This call hold all the saved batches and all there commands
    """
    __instance = None
    __batches = {}

    def __new__(cls, *args, **kwargs):
        if not Batch_holder.__instance:
            Batch_holder.__instance = object.__new__(cls)
        return Batch_holder.__instance

    def get_batches(self):
        return self.__batches

    def add_batch(self, batch_name, batch_commands):
        """
        Add a new batch with name to the batch dictionary
        """
        if batch_name in self.__batches.keys():
            raise Exception("This batchname already")
        self.__batches[batch_name] = batch_commands

    def get_batch_by_name(self, batch_name):
        """
        Get the patch array by the name
        param: Batch name to get is batch commands array
        """
        try:
            return self.__batches[batch_name]
        except Exception:
            raise Exception("This batch is not saved")

    def get_batches_name(self):
        """
        Return all the batches' name
        """
        return self.__batches.keys()



