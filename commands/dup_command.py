from commands.command import Command
from dna_sequences.dna import DNA


class Dup_command(Command):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Dup_command.__instance:
            Dup_command.__instance = object.__new__(cls)
        return Dup_command.__instance

    def run_command(self, command):
        """
        duplicates the sequence.
        If a new name is not provided, then it will be based on the name of <seq>, suffixed
        by number
        :param command:Dup command to run
        :return: Result printed
        """
        command = command.split(" ")
        if not 2 <= len(command) <= 3 or (len(command) > 2 and not command[2].startswith('@')):
            return "in valid command"
        try:
            dna = super().get_dna_holder().get_dna_by_id_or_name(command[1])
        except Exception as error:
            return error
        name = command[2].replace('@', '') if len(command) > 2 else None

        if super().get_dna_holder().check_sequence_in_the_dna(name) or not name:
            index = 1
            name = f"{dna.get_sequence_name()}_{index}"
            while super().get_dna_holder().check_sequence_in_the_dna(name):
                name = f"{dna.get_sequence_name()}_{index}"
                index += 1
        try:
            return super().get_dna_holder().add_dna(dna.get_dna(), name)
        except Exception as error:
            return error

    # def duplicate(self, sequence_id, name=None):
    #     dna = super().get_dna_holder().get_dna_by_id_or_name(co)
    #     for dna in super().get_dna_holder():
    #         if dna.get_sequence_id() == int(sequence_id):
    #             if not name or super().get_dna_holder().check_sequence_in_the_dna(name):
    #                 index = 1
    #                 while super().get_dna_holder().check_sequence_in_the_dna(name) or not name:
    #                     name = f"{dna.get_sequence_name()}_{index}"
    #                     index += 1
    #             try:
    #                 return super().get_dna_holder().add_dna(dna.get_dna, name)
    #                 # super().get_dna_holder().get_dna_sequence().append(DNA(dna.get_dna(), name, len(super().get_dna_holder())))
    #             except Exception as error:
    #                 return error
    #             # return str(self.__dna_sequences[-1])
    #     return "this id is not in the data"
