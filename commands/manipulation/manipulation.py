import copy

from commands.command import Command


class Sequence(Command):
    def run_command(self, command):
        command = command.split(" ")
        try:
            try:
                dna = super().get_dna_holder().get_dna_by_id_or_name(command[1])
            except Exception as error:
                raise error
            if ":" in command:
                if not command[-1].startswith('@'):
                    raise Exception("in valid command")
                new_dna = copy.deepcopy(dna)
                if command[-1] != '@@':
                    new_dna.set_name(command[-1].replace('@', ""))
                super().get_dna_holder().add_dna_object(new_dna)
                return super().get_dna_holder().get_dna_sequence()[-1], command[1:-2], command[-1].replace('@', "") if command[-1] != "@@" else None
            else:
                return dna, command[1:]

        except Exception as error:
            if not error:
                raise Exception("in valid command")
            raise error



