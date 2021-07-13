from commands.factory import Factory


class Invoker:
    def __init__(self):
        self.__factory = Factory()

    def get_factory(self):
        return self.__factory

    def run_command(self, command_to_run):
        """
        Running the correct command according to the factory
        :param command_to_run
        :return: The command's result
        """
        try:
            command = self.__factory.get_command(command_to_run.split(" ")[0])
            return command.run_command(command_to_run)
        except ValueError:
            return "in valid command"
