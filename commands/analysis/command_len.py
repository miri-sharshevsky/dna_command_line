from commands.command import Command


class Len(Command):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Len.__instance:
            Len.__instance = object.__new__(cls)
        return Len.__instance

    def run_command(self, command):
        """
        Return the length of the sequence.
        Required command: len <seq_id>
        """
        try:
            command = command.split(" ")
            if len(command) != 2 or not command[1].startswith('#'):
                raise Exception("In valid len parameters")
            c = command[1][1:]
            return len(super().get_dna_holder().get_dna_by_id(int(command[1][1:])))
        except Exception as error:
            return error
