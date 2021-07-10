from commands.manipulation.manipulation import Sequence


class Slice(Sequence):
    def run_command(self, command):
        try:
            command = super().run_command(command)
        except Exception as error:
            return error
        if 3 != len(command[1]) and len(command[1]) != 5:
            super().get_dna_holder().dell_dna(command[0])
            return "In valid slice arguments"
        if len(command[0].get_dna()) < int(command[1][2]):
            super().get_dna_holder().dell_dna()
            return "indexes are out of sequence"
        command[0].set_dna(command[0].get_dna()[int(command[1][1]): int(command[1][2])])
        return str(command[0])



