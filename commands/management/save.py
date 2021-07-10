from commands.management.management import Management


class Save(Management):
    def run_command(self, command):
        try:
            command = super().run_command(command)
        except Exception as error:
            return error
        if not 1 <= len(command[1]) <= 2:
            return "in valid save command"
        if len(command[1]) == 1:
            command[1].append(f"{command[0].get_sequence_name()}.rawdna")
        try:
            with open(command[1][1], 'w') as file:
                file.write(command[0].get_dna())
        except Exception:
            return "in valid file path"
