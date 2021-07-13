from commands.subject.subject import Subject


class Submit(Subject):
    """
    Class witch wait for submit from the user - it is observer of subject
    """
    def __init__(self):
        super().__init__()


    def wait_for_submit(self, input_method):
        print(input_method)
        submit = input(">confirm >>>")
        while submit.lower() != 'n' and submit.lower() != 'y':
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
            submit = input(">confirm >>>")
        if submit.lower() == 'n':
            super().notify(False)
        else:
            return super().notify(True)