class Observer:
    def __init__(self):
        self.observers = []

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)


class ChangeListen(Observer):
    def __init__(self):
        super().__init__()
        self._gain = 0

    @property
    def gain(self):
        return self._gain

    @gain.setter
    def gain(self, value):
        self._gain = value
        self.notify()

