from commands.manipulation.manipulation import manipulation


class Slice(manipulation):
    """
    Manipulation command witch slice the dna sequence and change it or
     save a new one according to the user input
    """
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Slice.__instance:
            Slice.__instance = object.__new__(cls)
        return Slice.__instance

    def run_command(self, command):
        """
        Slices the sequence, so that starts in <from_ind> (0-based index) and ends in <to_ind>
        :Return a string with the update dna
        Required command: slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]]
        """
        try:
            command = super().run_command(command)
        except Exception as error:
            return error
        if 3 != len(command[1]) and len(command[1]) != 5:
            if command[-1]:
                super().get_dna_holder().dell__last_dna(command[0])
            return "In valid slice arguments"
        if len(command[0].get_dna()) < int(command[1][2]):
            if command[-1]:
                super().get_dna_holder().dell__last_dna()
            return "indexes are out of sequence"
        command[0].set_dna(command[0].get_dna()[int(command[1][1]): int(command[1][2])])
        super().get_dna_holder().change_dna_status(command[0].get_sequence_id(), "menu")
        return str(command[0])



