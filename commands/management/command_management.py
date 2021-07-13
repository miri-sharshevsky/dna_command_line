import commands


class Management(commands.Command):
    """
    Class for all the management commands
    """
    def run_command(self, command):
        commands = command.split(" ")
        try:
            dna = super().get_dna_holder().get_dna_by_id_or_name(commands[1])
        except Exception as error:
            raise error
        if not dna:
            raise Exception("This sequence is not exists")
        return dna, commands[1:]