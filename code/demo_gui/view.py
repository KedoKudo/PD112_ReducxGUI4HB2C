#!/usr/bin/env python
"""simple demo GUI for MVP pattern"""

import sys
from qtpy.QtWidgets import (
    QApplication,
    QFrame,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class demoView(QWidget):
    def __init__(self, label="demoView", parent=None):
        super(demoView, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # top row
        self.toprow = QFrame(self)
        self.layout_toprow = QHBoxLayout(self.toprow)
        self.toprow.setLayout(self.layout_toprow)
        self.layout.addWidget(self.toprow)
        #
        self.label1 = QLabel("Cliked ? times")
        self.layout_toprow.addWidget(self.label1)

        # bottom row
        self.botrow = QFrame(self)
        self.layout_botrow = QHBoxLayout(self.botrow)
        self.botrow.setLayout(self.layout_botrow)
        self.layout.addWidget(self.botrow)
        #
        self.button_click = QPushButton("clike me")
        self.button_show = QPushButton("show")
        self.layout_botrow.addWidget(self.button_click)
        self.layout_botrow.addWidget(self.button_show)


if __name__ == "__main__":
    print("This is just a preview of the design")
    app = QApplication(sys.argv)
    view = demoView()
    view.show()
    app.exec_()