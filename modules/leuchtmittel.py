from modules.farbe import CFarbe


class CLeuchtmittel:
    def __init__(self, leistung: float, farbe: CFarbe, zustand: bool = False):
        self._leistung = leistung
        self._zustand = zustand
        self._farbe = farbe


class CLeuchte(CLeuchtmittel):

    ## Getter, Setter ##
    def getLeistung(self) -> float:
        return self._leistung

    def getZustand(self) -> bool:
        return self._zustand

    def getFarbe(self) -> CFarbe:
        return self._farbe

    def setLeistung(self, leistung: float):
        self._leistung = leistung

    ## Methodes ##
    def toggle(self) -> bool:
        if self._zustand:
            self._zustand = False
        else:
            self._zustand = True
        return self.getZustand()

    def schalten(self, zustand: bool) -> bool:
        self._zustand = zustand
        return self.getZustand()
