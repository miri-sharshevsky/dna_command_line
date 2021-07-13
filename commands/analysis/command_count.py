from commands.analysis.analysis import Analysis


class Count(Analysis):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Count.__instance:
            Count.__instance = object.__new__(cls)
        return Count.__instance

    def run_command(self, command):
        """
        Returns the number of instances of the sub-sequence within the larger sequence.
        Required command:  count <seq> <expressed_sub_seq> or count <seq_to_find_in> <seq_to_be_found>
        """
        try:
            command = super().run_command(command)
            return len(super().get_dna_holder().find_all_sub_sequence(command[1], command[2]))
        except Exception as error:
            return error
