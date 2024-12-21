"""

CP - current character, текущий игрок

"""
def SELECT(CP: number):
    if input.button_is_pressed(Button.B):
        CP = CP + 1
    elif input.button_is_pressed(Button.A):
        CP = CP - 1
    else:
        if CP == 1:
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
                """)
        elif CP == 2:
            basic.show_leds("""
                . . . . .
                . . # . .
                . # # # .
                . . # . .
                . . . . .
                """)
        elif CP == 3:
            basic.show_leds("""
                . . # # #
                . # # # #
                # # # # #
                # # # # .
                # # # . .
                """)
        else:
            pass
CP2 = 0
ffdasdasdaf = 1
_1 = 0
_2 = 0
CP2 = 1

def on_forever():
    if ffdasdasdaf == 1:
        SELECT(_1)
    elif ffdasdasdaf == 2:
        pass
    elif ffdasdasdaf == 3:
        pass
basic.forever(on_forever)
