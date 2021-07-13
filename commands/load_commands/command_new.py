from commands.load_commands.loads import Loads


class New_command(Loads):
    """
    Load command with add a new dna to the data base
    """
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not New_command.__instance:
            New_command.__instance = object.__new__(cls)
        return New_command.__instance

    def run_command(self, command):
        """
        Creates a new sequence, as described by the followed sequence.
        If the @<sequence_name> is used, then this will be the name of the new sequence.
        Otherwise, a default name will be provided
        Required command: new <sequence> [@<sequence_name>]
        """
        try:
            command = super().run_command(command)
            if not 2<=len(command) <= 3:
                raise Exception("in valid command")
            if super().get_dna_holder().check_sequence_in_the_dna(command[1]):
                command[1] = None
            return super().get_dna_holder().add_dna(command[0], command[1])
        except Exception as error:
            return error
