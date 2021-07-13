from commands import Command


class List(Command):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if not List.__instance:
            List.__instance = object.__new__(cls)
        return List.__instance


    def run_command(self, command):
        """
        shows all the sequences in the system, by order.
        Required command: list
        """
        commands_statuses = {
            "new": 'o',
            "files": '-',
            "menu": '*'
        }
        if command != "list":
            return "In valid list arguments"
        commands = []
        for dna in super().get_dna_holder().get_dna_sequence():
            commands.append(f"{commands_statuses[dna[1]]} {str(dna[0])}")
        return "\n".join(commands)