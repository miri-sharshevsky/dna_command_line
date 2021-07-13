DNA_chars = ['A', 'C', 'T', 'G']


def check_string_in_dna(dna_string):
    """
    Help function for checking if all the char in the string are correct
    :param dna_string: DNA to check
    :return: True or False
    """
    for char in dna_string:
        if char not in DNA_chars:
            return False
    return True


class DNA:
    def __init__(self, dna_sequence, dna_name, dna_id):
        if not check_string_in_dna(dna_sequence):
            raise Exception("The DNA must be with A, C, T and G chars only")
        self.__dna_name = dna_name
        self.__dna_id = dna_id
        self.__dna_sequence = dna_sequence

    def get_dna(self):
        return self.__dna_sequence

    def get_sequence_name(self):
        return self.__dna_name

    def get_sequence_id(self):
        return self.__dna_id

    def set_name(self, name):
        self.__dna_name = name

    def set_id(self, id):
        self.__dna_id = id

    def set_dna(self, dna_string):
        if not check_string_in_dna(dna_string):
            raise Exception("The DNA be must with A, C, T and G chars only")
        self.__dna_sequence = dna_string

    def insert(self, nucleotide_value, index):
        """
        gets nucleotide value and index and insert that
        value to match index
        :param nucleotide_value: Value to insrt
        :param index:Index to insert to
        """
        if not nucleotide_value in DNA_chars:
            raise Exception("The DNA be must with A, C, T and G chars only")
        try:
            dna_arr = list(self.__dna_sequence)
            dna_arr[index] = nucleotide_value
            self.__dna_sequence = "".join(dna_arr)
        except:
            raise Exception("This index is out of the DNA range")

    def assignment(self, other):
        if isinstance(other, DNA):
            self.__dna_sequence = other.get_dna()
        elif isinstance(other, str):
            self.__dna_sequence = other
        else:
            raise Exception("Invalid type for DNA assignment")

    #############################
    ### Overloading operators ###
    #############################

    def __str__(self):
        return f"[{self.__dna_id}] {self.__dna_name}: {self.__dna_sequence}"

    def __eq__(self, other):
        try:
            return self.__dna_sequence == other.get_dna()
        except ValueError:
            return False

    def __ne__(self, other):
        try:
            return self.__dna_sequence != other.get_dna()
        except ValueError:
            return True

    def __getitem__(self, key):
        try:
            return self.__dna_sequence[key]
        except IndexError as er:
            print(er)

    def __setitem__(self, key, value):
        try:
            value in DNA_chars
        except ValueError:
            print("nucleotide new value is not valid")
            dna_arr = list(self.__dna_sequence)
            dna_arr[key] = value
            self.__dna_sequence = "".join(dna_arr)

    def __len__(self):
        return len(self.__dna_sequence)


