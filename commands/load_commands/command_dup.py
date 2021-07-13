import commands


class Dup_command(commands.Command):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Dup_command.__instance:
            Dup_command.__instance = object.__new__(cls)
        return Dup_command.__instance

    def run_command(self, command):
        """
        duplicates the sequence.
        If a new name is not provided, then it will be based on the name of <seq>, suffixed
        by number
        :param command:Dup command to run
        Required command: dup <seq> [@<new_seq_name>]

        """
        command = command.split(" ")
        if not 2 <= len(command) <= 3 or (len(command) > 2 and not command[2].startswith('@')):
            return "in valid command"
        try:
            dna = super().get_dna_holder().get_dna_by_id_or_name(command[1])
        except Exception as error:
            return error
        name = command[2][1:] if len(command) > 2 else dna.get_sequence_name()
        try:
            return super().get_dna_holder().add_dna(dna.get_dna(), name)
        except Exception as error:
            return error


