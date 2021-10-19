from dataclasses import dataclass


@dataclass
class Counter:
    """
    Counter class

    Last edited: Oktober 18 2021
    |br| @author: ME

    """
    def __init__(self, start_value=0):
        """
        Constructor for creating an Counter class instance
        **Required arguments:**

        **Default arguments:**
        :param start_value: number on which the counter starts
            |br| * the default value is 0.
        :type start_value: positive integer
         
        """
        self.start_value = start_value
        self.counter = start_value

    def reset(self):
        """
        Function for reseting the counter.
        """
        self.counter = self.start_value

    def add(self, increment=1):
        """
        Function for adding an increment.
        **Default arguments:**
        :param increment: the increment to be added
            |br| * the default value is 1.
        :type increment: stricly positiv integer
        """
        self.counter += increment
