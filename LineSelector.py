import sys
import keyboard
Exit = 0


def c(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def r(text):
    r = 255
    g = b = 50
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def g(text):
    g = 255
    r = b = 50
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def b(text):
    b = 255
    r = g = 100
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


Line = 1

one = f"{g('> 1')}\n  2\n  3'"
two = f"  1\n{g('> 2')}\n  3'"
three = f"  1\n  2\n{g('> 3')}"



def linePrint(LineInt=1, TmpDown=0, TmpUp=0):
    if LineInt == 1:
        sys.stdout.write(f"\r{one}")
    if LineInt == 2:
        sys.stdout.write(f"\r{two}")
    if LineInt == 3:
        sys.stdout.write(f"\r{three}")



Down = 0
Up = 0

_Down = 0
_Up = 0

while Exit != 1:

    if keyboard.is_pressed("Down"):
        Up = 1
        _Up = 1

    if _Up != Up:
        if Line == 1:
            Line = 3
        else:
            Line = Line - 1
        linePrint(Line, _Down, _Up)
        _Up = 0

    if keyboard.is_pressed("Up"):
        Down = 1
        _Down = 1

    if _Down != Down:
        if Line == 1:
            Line = 3
        else:
            Line = Line - 1
        linePrint(Line, _Down, _Up)
        _Down = 0

    if not keyboard.is_pressed("z"):
        Up = 0

    if not keyboard.is_pressed("s"):
        Down = 0

      # DEBUG → sys.stdout.write(f"\r{Line}-TD={_Down} TU={_Up} D={Down} U={Up}")
