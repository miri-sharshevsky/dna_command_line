from commands.command import Command


class Analysis(Command):
    """
    Class for all the anlysis commands
    """

    def run_command(self, command):
        try:
            command = command.split(" ")
            if len(command) != 3:
                raise Exception("in valid arguments")
            if command[2].startswith('#') or command[2].startswith('@'):
                command[2] = super().get_dna_holder().get_dna_by_id_or_name(command[2]).get_dna()
            return command
        except Exception as error:
            raise error
