from dataclasses import dataclass


@dataclass
class Counter:
    def __init__(self, start_value=0):
        self.start_value = start_value
        self.counter = start_value

    def reset(self):
        self.counter = self.start_value

    def add(self, increment=1):
        self.counter += increment
