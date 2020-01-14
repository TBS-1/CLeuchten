from modules.leuchtmittel import CLeuchte
from modules.farbe import CFarbe
from modules.ampel import CAmpel
from tkinter import *


def startAmpel():
    root = Tk()
    ampel = CAmpel(root, "Ampel", 680, 200, 50)
    root.mainloop()


def testLeuchte():
    weisz = CFarbe(170, 16, 32)
    leuchti = CLeuchte(70.0, weisz, False)

    print("Test 1, State of leuchte")
    assert leuchti.getZustand() is False, "State of leuchte is True instead of False"
    leuchti.toggle()
    assert leuchti.getZustand() is True, "State of leuchte is False instead of True"
    leuchti.schalten(False)
    assert leuchti.getZustand() is False, "State of leuchte is True instead of True"
    print("Test 1, success")

    print("Test 2, Wattage of leuchte")
    assert leuchti.getLeistung() == 70.0, "Wattage is wrong(" + leuchti.getLeistung() + " instead of 70.0)"
    leuchti.setLeistung(50.0)
    assert leuchti.getLeistung() == 50.0, "Wattage is wrong(" + leuchti.getLeistung() + " instead of 50.0)"
    print("Test 2, success")

    print("Test 3, color as Hex and RGB")
    assert leuchti.getFarbe().getRGB() == (170, 16, 32)
    assert leuchti.getFarbe().getHex() == "#aa1020"
    leuchti.getFarbe().setRGB((54, 208, 117))
    assert leuchti.getFarbe().getRGB() == (54, 208, 117)
    assert leuchti.getFarbe().getHex() == "#36d075"

    leuchti.getFarbe().setHex("#cd1076")
    assert leuchti.getFarbe().getRGB() == (205, 16, 118)
    assert leuchti.getFarbe().getHex() == "#cd1076"

    leuchti.getFarbe().setHex("#32cd32")
    assert leuchti.getFarbe().getRGB() == (50, 205, 50)
    assert leuchti.getFarbe().getHex() == "#32cd32"

    print("Test 3, success")


def argHandler(args: list):
    args.pop(0)
    if len(args) == 1:
        if "leuchtmittel" in args:
            print("Leuchtmittel enabled")
            testLeuchte()
        elif "ampel" in args:
            print("Ampel enabled")
            startAmpel()
    else:
        print("Starting program without parameters.")


def main():
    argHandler(sys.argv)


if __name__ == '__main__':
    main()
