import os

from dna_sequences.dna import DNA


class DNA_holder:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DNA_holder.__instance:
            DNA_holder.__instance = object.__new__(cls)
        return DNA_holder.__instance

    def __init__(self):
        self.__dna_sequences = []

    def get_dna_sequence(self):
        return self.__dna_sequences

    def add_dna_object(self, dna):
        return self.add_dna(dna.get_dna(), dna.get_sequence_name())

    def add_dna(self, sequence, name=None):
        """
        Add a new dna sequence
        :param sequence: Sequence for the new dna
        :param name: Name for the new dna
        :return: String
        """
        if not name or self.check_sequence_in_the_dna(name):
            name = f"seq{len(self.__dna_sequences)}"
        try:
            self.__dna_sequences.append(
                DNA(sequence, name, len(self.__dna_sequences)))
            return str(self.__dna_sequences[-1])
        except Exception as error:
            raise error

    def get_dna_by_id_or_name(self, identify):
        if identify.startswith('@'):
            return self.get_dna_by_name(identify.replace('@', ""))
        if identify.startswith('#'):
            return self.get_dna_by_id(int(identify.replace('#', '')))
        raise Exception("in valid request")

    def get_dna_by_id(self, sequence_id):
        for dna in self.__dna_sequences:
            if dna.get_sequence_id() == sequence_id:
                return dna
        raise Exception("this dna not founed")

    def get_dna_by_name(self, sequence_name):
        for dna in self.__dna_sequences:
            if dna.get_sequence_name() == sequence_name:
                return dna
        raise Exception("this dna not founed")



    def dell_dna(self):
        try:
            string = f"Deleted: [{self.__dna_sequences[-1].get_sequence_id()}] {self.__dna_sequences[-1].get_sequence_name()}: {self.__dna_sequences[-1].get_dna()}"
            self.__dna_sequences.pop()
            return string
        except ValueError as error:
            return error

    def get_dna_by_sequence(self, sequence):
        for dna in self.__dna_sequences:
            if dna.get_dna() == sequence:
                return dna

    def duplicate_sequences(self, sequence_id, name=None):
        """
        duplicates the sequence.
        If a new name is not provided, then it will be based on the name of <seq>, suffixed
        by "_number"
        :param sequence_id: Id of sequence to duplicate
        :param name: New name for the duplicated sequence
        :return:
        """
        for dna in self.__dna_sequences:
            if dna.get_sequence_id() == int(sequence_id):
                if not name or self.check_sequence_in_the_dna(name):
                    index = 1
                    while self.check_sequence_in_the_dna(name) or not name:
                        name = f"{dna.get_sequence_name()}_{index}"
                        index += 1
                try:
                    self.__dna_sequences.append(DNA(dna.get_dna(), name, len(self.__dna_sequences)))
                except Exception as error:
                    return error
                return str(self.__dna_sequences[-1])
        return "this id is not in the data"

    def check_sequence_in_the_dna(self, sequence_name):
        """
        Help function to check if a sequence name is already used
        :param sequence_name: Name to check for
        :return: True or False
        """
        for dna in self.__dna_sequences:
            if dna.get_sequence_name() == sequence_name:
                return True
        return False
