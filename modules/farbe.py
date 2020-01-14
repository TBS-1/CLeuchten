class CFarbe:
    def __init__(self, red: int, green: int, blue: int):
        self._rgb: tuple = (red, green, blue)
        self.r = red
        self.g = green
        self.b = blue

    ## Getter, Setter ##
    def getRGB(self) -> tuple:
        return self._rgb

    def getHex(self) -> str:
        return '#%02x%02x%02x' % self._rgb

    def getR(self) -> int:
        return self.r

    def getG(self) -> int:
        return self.g

    def getB(self) -> int:
        return self.b

    def setRGB(self, rgb: tuple):
        self._rgb = rgb

    def setHex(self, value):
        value = value.lstrip('#')
        self.setRGB(tuple(int(value[i:i+2], 16) for i in (0, 2, 4)))
