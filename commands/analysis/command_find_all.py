from commands.analysis.analysis import Analysis


class Find_all(Analysis):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Find_all.__instance:
            Find_all.__instance = object.__new__(cls)
        return Find_all.__instance

    def run_command(self, command):
        """
        Return all the indices where the sub-sequence appears.
        Required command:  findall <seq> <expressed_sub_seq> or findall <seq_to_find_in> <seq_to_be_found>
        """
        try:
            command = super().run_command(command)
            return super().get_dna_holder().find_all_sub_sequence(command[1], command[2])

        except Exception as error:
            return error