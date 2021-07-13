from commands.subject import Submit
from commands.management.command_management import Management


class Del(Management):
    """
    Del a dna from the database with dna's id or dna's name
    Before deleting waiting for a sign from the submit observer
    """
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Del.__instance:
            Del.__instance = object.__new__(cls)
        return Del.__instance

    def __init__(self):
        self.__dell_dna = None
        self.__submit = Submit()
        self.__submit.attach(self)

    def run_command(self, command):
        """
        deletes a sequence.
        Required command: del <seq>
        """
        try:
            commands = super().run_command(command)
        except Exception as error:
            return error
        if len(commands[1]) != 1:
            return "Invalid command arguments"
        self.__dell_dna = commands[0]
        return self.__submit.wait_for_submit(
            f"Do you really want to delete {commands[0].get_sequence_name()}: {commands[0].get_dna()}? Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'")

    def update(self, command):
        """
        Calls when the sign is given from the submit subject
        """
        if command:
            return super().get_dna_holder().dell_dna(self.__dell_dna)
        else:
            return "The delete command canceled"
