from dna_sequences.dna_holder import DNA_holder


class Command:
    """
    Interface for all the cli commands
    """
    __dna_holder = DNA_holder()

    def get_dna_holder(self):
        return self.__dna_holder

    def run_command(self, command):
        raise