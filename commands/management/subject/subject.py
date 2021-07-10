class Subject:
    """Represents what is being observed"""

    def __init__(self):
        self._observers = []

    def notify(self,command, dna, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                return observer.update(command, dna)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
