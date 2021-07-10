from commands.command import Command


class Parser(Command):
    def run_command(self, command):
        command = command.split(" ")
        if not 2 <= len(command) <= 3 or (len(command) > 2 and not command[2].startswith('@')):
            return "iv valid command"
        return [command[1], command[2].replace("@", "") if len(command) == 3 else None]
