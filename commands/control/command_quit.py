from commands import Command, Submit


class Quit(Command):
    """
    Exit from the command waitng before to a sign from the user in the submit observer
    """
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not Quit.__instance:
            Quit.__instance = object.__new__(cls)
        return Quit.__instance

    def __init__(self):
        self.__submit = Submit()
        self.__submit.attach(self)

    def run_command(self, command):
        """
        prints a goodbye message and exists the application.
        Required command: quit
        """
        if command != "quit":
            return "in valid quit arguments"
        statuses = super().get_dna_holder().get_statuses_state()
        return self.__submit.wait_for_submit(f"There are {statuses['menu']} modified and {statuses['new']} sequnces, Are you sure you "
                                             f"want to quit? \n Please confirm b 'y' or 'y' or cencel by 'n' or 'N'")

    def update(self, command):
        """

        """
        if command:
            return "Command_Stopped"

