import commands


class Loads(commands.Command):
    """
    Class for all the management commands
    """
    def run_command(self, command):
        command = command.split(" ")
        if not 2 <= len(command) <= 3 or (len(command) > 2 and not command[2].startswith('@')):
            raise Exception("iv valid command")
        return [command[1], command[2][1:] if len(command) == 3 else None]
