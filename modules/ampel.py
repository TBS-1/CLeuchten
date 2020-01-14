from tkinter import *

from modules.farbe import CFarbe
from modules.leuchtmittel import CLeuchte


def writeCircle(canvas: Canvas, x, y, size, outline_color: CFarbe, fill_color: CFarbe, outline_width=2):
    canvas.create_oval(x + outline_width, y + outline_width, x + size, y + size, outline=outline_color.getHex(),
                       fill=fill_color.getHex(), width=outline_width)


class CGrafikleuchte(CLeuchte):
    def __init__(self, master: Tk, canvas: Canvas, x: int, y: int, size: int,
                 color_lit: CFarbe, state: bool = False):

        self.master = master
        self.canvas = canvas
        self.y = y
        self.x = x
        self.size = size
        self.state = state

        self.color_lit = color_lit

        i = 0
        dark = [0, 0, 0]
        assertion = True
        while i != len(color_lit.getRGB()):
            if color_lit.getRGB()[i] > 50:
                dark[i] = int(color_lit.getRGB()[i] - 50)
                assertion = False
            i += 1
        assert not assertion, "The lit color you chose is too dark (" + str(color_lit.getRGB()) + ")"
        self.color_dark = CFarbe(dark[0], dark[1], dark[2])

        self._createGLeuchte(self.color_dark)

    def _createGLeuchte(self, fill_color: CFarbe, outline_width=2):
        self.canvas.create_oval(self.x + outline_width, self.y + outline_width, self.x + self.size, self.y + self.size,
                                outline=CFarbe(105, 105, 105).getHex(), fill=fill_color.getHex(), width=outline_width)

    def toggle(self):
        super().toggle()
        if self.getZustand():
            self._createGLeuchte(self.color_lit)
        else:
            self._createGLeuchte(self.color_dark)

    def schalten(self, zustand: bool):
        super().schalten(zustand)

        if self.getZustand():
            self._createGLeuchte(self.color_lit)
        else:
            self._createGLeuchte(self.color_dark)


class CAmpel:

    def __init__(self, master: Tk, w_name: str, w_height: int, w_width: int, speed: int):
        self.speed = speed
        self.switching = False
        self.state = 0
        self.master = master
        self.__geometry = str(w_width) + "x" + str(w_height)
        self.__w_name = w_name

        self.master.title(self.__w_name)
        self.master.geometry(self.__geometry)

        self.red_color = CFarbe(255, 0, 0)
        self.yellow_color = CFarbe(255, 255, 0)
        self.green_color = CFarbe(0, 255, 0)
        self.a_frame_background = CFarbe(255, 255, 255)

        self.ampelFrame = Frame(master=self.master, background=self.a_frame_background.getHex())
        self.ampelFrame.place(x=0, y=0, width=200, height=680)

        button_toggle = Button(self.ampelFrame, text="Next", height=1, command=self.switch)
        button_toggle.pack(fill=X)
        button_start_switching = Button(self.ampelFrame, text="Start switching", height=1, command=self.startSwitching)
        button_start_switching.pack(fill=X)
        button_reset = Button(self.ampelFrame, text="Reset/Stop switching", height=1, command=self.reset)
        button_reset.pack(fill=X)

        self.canvas = Canvas(self.ampelFrame)

        self.green = CGrafikleuchte(self.master, self.canvas, 0, 400, 196, self.green_color)
        self.yellow = CGrafikleuchte(self.master, self.canvas, 0, 200, 196, self.yellow_color)
        self.red = CGrafikleuchte(self.master, self.canvas, 0, 0, 196, self.red_color)

        self.canvas.pack(fill=BOTH, expand=1)

    def getState(self):
        return self.state

    def setState(self, index):
        if index == 0:
            self.green.schalten(False)
            self.yellow.schalten(False)
            self.red.schalten(False)
        elif index == 1:
            self.green.schalten(True)
            self.yellow.schalten(False)
            self.red.schalten(False)
        elif index == 2:
            self.green.schalten(False)
            self.yellow.schalten(True)
            self.red.schalten(False)
        elif index == 3:
            self.green.schalten(False)
            self.yellow.schalten(False)
            self.red.schalten(True)
        elif index == 4:
            self.green.schalten(False)
            self.yellow.schalten(True)
            self.red.schalten(True)
        else:
            self.state = 0
            return
        self.state = index

    def switch(self):
        state = self.getState() + 1
        if state <= 4:
            self.setState(state)
        else:
            self.setState(1)

    def startSwitching(self):
        self.switching = True
        if self.getState() == 0:
            self.setState(2)
        self.__stSw()

    def __stSw(self):
        if self.switching is True:
            if self.getState() == 1:
                self.switch()
                self.master.after(int(3 / 100 * self.speed) * 1000, self.__stSw)
            elif self.getState() == 2:
                self.switch()
                self.master.after(int(20 / 100 * self.speed) * 1000, self.__stSw)
            elif self.getState() == 3:
                self.switch()
                self.master.after(int(3 / 100 * self.speed) * 1000, self.__stSw)
            elif self.getState() == 4:
                self.switch()
                self.master.after(int(20 / 100 * self.speed) * 1000, self.__stSw)

    def reset(self):
        self.switching = False
        self.setState(0)
