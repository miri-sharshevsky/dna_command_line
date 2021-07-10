from commands.manipulation.manipulation import Sequence


class Replace(Sequence):
    def run_command(self, command):
        try:
            command = super().run_command(command)
        except Exception as error:
            return error
        changes = [(int(command[1][i]),command[1][i+1]) for i in range(1, len(command[1]), 2)]
        seq = command[0].get_dna()
        for tup in changes:
            if len(seq) <= tup[0]:
                super().get_dna_holder().dell_dna()
                return "indexes out of sequences range"
            seq = seq[:tup[0]] + tup[1] + seq[tup[0]+1:]
        try:
            command[0].set_dna(seq)
        except Exception as error:
            super().get_dna_holder().dell_dna(command[0])
            return error
        return str(command[0])