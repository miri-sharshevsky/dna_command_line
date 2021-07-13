from commands.manipulation.manipulation import manipulation


class Replace(manipulation):
    """
    Manipulation command witch replace the given indexes with the given new values
    and chang or save the new dna according to the user input
    """
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Replace.__instance:
            Replace.__instance = object.__new__(cls)
        return Replace.__instance

    def run_command(self, command):
        """
        replaces the letter in the (0-based) index of <seq> by <new_letter>.
        """
        try:
            command = super().run_command(command)
        except Exception as error:
            return error
        changes = [(int(command[1][i]),command[1][i+1]) for i in range(1, len(command[1]), 2)]
        seq = command[0].get_dna()
        for tup in changes:
            if len(seq) <= tup[0]:
                if command[-1]:
                    super().get_dna_holder().dell__last_dna()
                return "indexes out of sequences range"
            seq = seq[:tup[0]] + tup[1] + seq[tup[0]+1:]
        try:
            command[0].set_dna(seq)
        except Exception as error:
            if command[-1]:
                super().get_dna_holder().dell__last_dna(command[0])
            return error
        super().get_dna_holder().change_dna_status(command[0].get_sequence_id(), "menu")
        return str(command[0])