from commands.management.management import Management
from commands.management.subject.submit import Submit


class Dell(Management):
    def __init__(self):
        self.__submit = Submit()
        self.__submit.attach(self)

    def run_command(self, command):
        try:
            commands = super().run_command(command)
        except Exception as error:
            return error
        if len(commands) != 2:
            return Exception("Invalid command arguments")
        return self.__submit.wait_for_submit(
            f"Do you really want to delete {commands[0].get_sequence_name()}: {commands[0].get_dna()}? Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'",
            commands[0])

    def update(self, command, dna):
        if command:
            return super().get_dna_holder().dell_dna(dna)
        else:
            return "The delete command canceled"
