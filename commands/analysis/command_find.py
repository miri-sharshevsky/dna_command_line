from commands.analysis.analysis import Analysis


class Find(Analysis):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Find.__instance:
            Find.__instance = object.__new__(cls)
        return Find.__instance

    def run_command(self, command):
        """
        Returns the (0-based) index of the first appearance of <expressed_sub_seq> in
            the sequence <seq>.
        Required command:  find <seq> <expressed_sub_seq> or find <seq_to_find_in> <seq_to_be_found>
        """
        try:
            command = super().run_command(command)
            return super().get_dna_holder().find_sub_sequence(command[1], command[2])

        except Exception as error:
            return error

