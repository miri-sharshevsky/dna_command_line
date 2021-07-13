from commands.batch.batch import Batch


class Saving_batch(Batch):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Saving_batch.__instance:
            Saving_batch.__instance = object.__new__(cls)
        return Saving_batch.__instance

    def run_command(self, command):
        """
        Saving the batch in a file
        Required command:  batchsave <@batch_name>
        """
        command = command.split(" ")
        if not 2<= len(command) <= 3:
            return "in valid batchsave aguments"
        try:
            batch = super().get_batch_holder().get_batch_by_name(command[1])
        except Exception as error:
            return error
        if len(command) == 2:
            command.append(f"{command[1]}.dnabatch")
        with open(command[2], 'w') as file:
            for command in batch:
                file.write(f"{command}\n")