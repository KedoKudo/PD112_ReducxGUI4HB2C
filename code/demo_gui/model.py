#!/usr/bin/env python
"""simple demo GUI for MVP pattern"""


class demoModel:
    def __init__(self):
        self.__counts = 0  # track # of clicks
        self.__instructions = []  #

    @property
    def counts(self):
        return self.__counts

    def register_click(self, *args, **kwargs):
        """return a function"""
        print("register a click, not evalute right away")

        def inner(self, *args, **kwargs):
            self.__counts += 1

        self.__instructions.append(inner)

    def show_clicks(self):
        # evalute the instruction list now
        for me in self.__instructions:
            me(self)
        print(f"Total # of clicks = {self.__counts}")
        # print the total instruction cached
        print("Cached clicks action so far")
        for me in self.__instructions:
            print(me)
        # reset the list
        self.__instructions = []


if __name__ == "__main__":
    print("Model should be free of GUI related elements.")