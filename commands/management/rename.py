from commands.management.management import Management


class Rename(Management):
    def run_command(self, command):
        try:
            commands = super().run_command(command)
            if len(commands) != 2 or not commands[1][-1].startswith('@'):
                return "in valid rename arguments"
            name = commands[1][-1].replace('@', '')
            if super().get_dna_holder().check_sequence_in_the_dna(name):
                return "This name is already used"
            commands[0].set_name(name)

        except Exception as error:
            return error




