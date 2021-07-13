from commands.management.command_management import Management


class Save(Management):
    """
    Management command witch save the given dna's sequence in a file
    The file's path is given from the user or create with the dna's name with suffix .rawdna
    """
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Save.__instance:
            Save.__instance = object.__new__(cls)
        return Save.__instance

    def run_command(self, command):
        """
        saves sequence <seq> to a file.
        Required command: save <seq> [<filename>]
        """
        try:
            command = super().run_command(command)
        except Exception as error:
            return error
        if not 1 <= len(command[1]) <= 2:
            return "in valid save command"
        if len(command[1]) == 1:
            command[1].append(f"{command[0].get_sequence_name()}.rawdna")
        try:
            with open(command[1][1], 'w') as file:
                super().get_dna_holder().change_dna_status(command[0].get_sequence_id(), "files")
                file.write(command[0].get_dna())
        except Exception as r:
            return "in valid file path"
