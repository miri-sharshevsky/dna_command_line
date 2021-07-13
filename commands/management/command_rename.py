from commands.management.command_management import Management


class Rename(Management):
    """
    Management command with rename a dna name
    """
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Rename.__instance:
            Rename.__instance = object.__new__(cls)
        return Rename.__instance

    def run_command(self, command):
        """
        renames the name of the sequence to the new name.
        Required command: rename <seq> @<new_name>
        """
        try:
            commands = super().run_command(command)
            if len(commands) != 2 or not commands[1][-1].startswith('@'):
                raise Exception("in valid rename arguments")
            name = commands[1][-1][1:]
            if super().get_dna_holder().check_sequence_in_the_dna(name):
                return "This name is already used"
            commands[0].set_name(name)

        except Exception as error:
            return error




