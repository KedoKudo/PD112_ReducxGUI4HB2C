#!/usr/bin/env python
"""simple demo GUI for MVP pattern"""

import sys
from qtpy.QtWidgets import QApplication

from view import demoView
from model import demoModel


class demoPresenter:
    def __init__(self):
        self.__view = demoView()
        self.__model = demoModel()
        # connect signal and slots
        self.__view.button_click.clicked.connect(self.track)
        self.__view.button_show.clicked.connect(self.display_clicks)

    def show(self):
        self.__view.show()

    def track(self):
        self.__model.register_click()
        print(f"counts = {self.__model.counts}")

    def display_clicks(self):
        self.__model.show_clicks()
        self.__view.label1.setText(f"Cliked {self.__model.counts} times")


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    demo = demoPresenter()
    demo.show()
    app.exec_()