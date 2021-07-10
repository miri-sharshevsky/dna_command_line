import os
from commands.parser import Parser
from dna_sequences.dna import DNA


class Load_command(Parser):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Load_command.__instance:
            Load_command.__instance = object.__new__(cls)
        return Load_command.__instance


    def run_command(self, command):
        """
        loads the sequence from the file, assigns it with a number (ID) and a default name, if
        one was not provided
        :param command: Load command to run
        :return:The result printed
        """
        command = super().run_command(command)
        if type(command) == str:
            return command
        if '.' not in command[0]:
            command[0] += '.rawdna'
        try:
            return self.add_dna_sequences_from_file(command[0], command[1]if len(command) > 1 else None)
        except:
            return "in valid file path"


    def add_dna_sequences_from_file(self, file_path, name=None):
        """
        Add a new dna sequence from a file
        :param file_path: File to get th sequence
        :param name: Name for the dna
        :return: Str of the new dna
        """
        try:
            with open(file_path, 'w') as dna_file:
                sequence = dna_file.readline()
        except Exception:
            raise Exception("in valid file path")

        if not name:
            name = os.path.splitext(os.path.basename(file_path))[0]
            index = 1
            while super().get_dna_holder().check_sequence_in_the_dna(name):
                name = f"{os.path.splitext(os.path.basename(file_path))[0]}_{index}"
                index += 1
        try:
            dna = super().get_dna_holder().add_dna(sequence, name)
        except Exception as error:
            raise error
        if len(dna.get_dna()) > 40:
            sequence = sequence[0:31] + "..." + sequence[-3:]
        else:
            sequence = dna.get_dna()
        return f"[{dna.get_sequence_id()}] {dna.get_sequence_name()}: {sequence}"