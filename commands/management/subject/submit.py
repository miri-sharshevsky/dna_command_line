from commands.management.subject.subject import Subject


class Submit(Subject):
    def __init__(self):
        super().__init__()


    def wait_for_submit(self, input_method, dna):
        print(input_method)
        submit = input(">confirm >>>")
        while submit.lower() != 'n' and submit.lower() != 'y':
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
            submit = input(">confirm >>>")
        if submit.lower() == 'n':
            super().notify(False, dna)
        else:
            return super().notify(True, dna)