import data_base


class Command:
    """
    Interface for all the clit commands
    """
    __dna_holder = data_base.DNA_holder()

    def get_dna_holder(self):
        return self.__dna_holder

    def run_command(self, command):
        raise