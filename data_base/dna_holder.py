from data_base.dna import DNA


class DNA_holder:
    """
    This class hold all the dnas and all the commands witch change them
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DNA_holder.__instance:
            DNA_holder.__instance = object.__new__(cls)
        return DNA_holder.__instance

    def __init__(self):
        self.__dna_sequences = []

    def get_dna_sequence(self):
        return self.__dna_sequences

    def add_dna_object(self, dna, status="new"):
        """
        add a new dna object
        """
        return self.add_dna(dna.get_dna(), dna.get_sequence_name(), status)

    def add_dna(self, sequence,  name=None, status="new"):
        """
        Add a new dna sequence
        :param sequence: Sequence for the new dna
        :param name: Name for the new dna
        :param status: The status will be for the new dna
        :return: String
        """
        if not name or self.check_sequence_in_the_dna(name):
            name = self.get_next_name(name) if name else self.get_next_name('seq')
        try:
            self.__dna_sequences.append([
                DNA(sequence, name, len(self.__dna_sequences)), status])
            return str(self.__dna_sequences[-1][0])
        except Exception as error:
            raise error

    def get_dna_by_id_or_name(self, identify):
        """
        Get the dna by id if get # or by name if get @
        """
        if identify.startswith('@'):
            return self.get_dna_by_name(identify.replace('@', ""))[0]
        if identify.startswith('#'):
            return self.get_dna_by_id(int(identify.replace('#', '')))[0]
        raise Exception("in valid request")

    def get_dna_by_id(self, sequence_id):
        """
        Get the dna object by id
        """
        for dna in self.__dna_sequences:
            if dna[0].get_sequence_id() == sequence_id:
                return dna
        raise Exception("this dna not founed")

    def get_dna_by_name(self, sequence_name):
        """
        Get the dna object by name
        """
        for dna in self.__dna_sequences:
            if dna[0].get_sequence_name() == sequence_name:
                return dna
        raise Exception("this dna not founed")

    def dell__last_dna(self):
        """
        Delete the last dna from the dna array
        """
        try:
            string = f"Deleted: [{self.__dna_sequences[-1][0].get_sequence_id()}] {self.__dna_sequences[-1].get_sequence_name()}: {self.__dna_sequences[-1].get_dna()}"
            self.__dna_sequences.pop()
            return string
        except ValueError as error:
            return error

    def dell_dna(self, dna):
        """
        Delete the getting dna from the dna array
        """
        index = None
        for d in self.__dna_sequences:
            if d[0] == dna:
                index = self.__dna_sequences.index(d)
        try:
            self.__dna_sequences.pop(index)
        except Exception:
            pass

    def check_sequence_in_the_dna(self, sequence_name):
        """
        Help function to check if a sequence name is already used
        :param sequence_name: Name to check for
        :return: True or False
        """
        for dna in self.__dna_sequences:
            if dna[0].get_sequence_name() == sequence_name:
                return True
        return False

    def get_next_name(self, name, sign='_'):
        """
        Get the next free name in the dna array with the name and the sign
        """
        index = 1
        new_name = f"{name}{sign}{index}"
        while self.check_sequence_in_the_dna(new_name):
            index += 1
            new_name = f"{name}{sign}{index}"
        return new_name

    def find_sub_sequence(self, dna, sub_sequence):
        """
        Find the index of the sub_sequence in the getting dna
        """
        try:
            return self.get_dna_by_id_or_name(dna).get_dna().find(sub_sequence)
        except Exception as error:
            raise error

    def find_all_sub_sequence(self, dna, sub_sequence):
        """
        Find all the indexes of the sub_sequence in the getting dna
        """
        try:
            dna_seq = self.get_dna_by_id_or_name(dna).get_dna()
            res = [i for i in range(len(dna_seq)) if dna_seq.startswith(sub_sequence, i)]
            return res
        except Exception as error:
            raise error

    def change_dna_status(self, dna_id, new_status):
        """
        Get a dna and a new status and change for the dna the status to the new status
        """
        for i in range(len(self.__dna_sequences)):
            if self.__dna_sequences[i][0].get_sequence_id() == dna_id:
                self.__dna_sequences[i][1] = new_status

    def get_statuses_state(self):
        """
        Return a dict with all the statuses and the number of the dna with that statuses
        """
        status_dict = {
            "new": 0,
            "files": 0,
            "menu": 0
        }
        for dna in self.__dna_sequences:
            status_dict[dna[1]] += 1
        return status_dict