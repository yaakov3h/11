def on_pin_pressed_p0():
    pass
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_gesture_shake():
    basic.show_leds("""
        . . . . .
                # . . # .
                # . # . #
                # . . # .
                . . . . .
    """)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def no_lamed():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # . . . .
                # . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # . . .
                . # . . .
                # . . . .
                . . . . .
    """)
    basic.show_leds("""
        # . . . .
                # # # . .
                . . # . .
                . # . . .
                # . . . .
    """)
    basic.show_leds("""
        . # . . .
                . # # # .
                . . . # .
                . . # . .
                . # . . .
    """)
    basic.show_leds("""
        . . # . .
                . . # # #
                . . . . #
                . . . # .
                . . # . .
    """)
    basic.show_leds("""
        . . . # .
                . . . # #
                . . . . .
                . . . . #
                . . . # .
    """)
    basic.show_leds("""
        . . . . #
                . . . . #
                . . . . .
                . . . . .
                . . . . #
    """)
def no_yud():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # . . . .
                # . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # . . .
                . # . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # # . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # # .
                . . . # .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . # #
                . . . . #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . #
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def no_alef():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # . . . .
                # . . . .
                . . . . .
                # . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # . . .
                . # . . .
                # . . . .
                . # . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                # . # . .
                . # . . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                # . . # .
                . # . # .
                # . # . .
                # . . # .
    """)
    basic.show_leds("""
        . . . . .
                . # . . #
                . . # . #
                . # . # .
                . # . . #
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . . . # .
                . . # . #
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . # .
                . . . . #
                . . . # .
                . . . # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . #
                . . . . .
                . . . . #
                . . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)

def on_pin_pressed_p2():
    music.play_melody("C D E F G A B C5 ", 90)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def no_koach():
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . . .
                # . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # . . . .
                . # . . .
                . # . . .
                # . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # . . .
                . . # . .
                . . # . .
                # # . . .
    """)
    basic.show_leds("""
        . . . . .
                . # # . .
                . . . # .
                . . . # .
                . # # . .
    """)
    basic.show_leds("""
        . . . . .
                . . # # .
                . . . . #
                . . . . #
                . . # # .
    """)
    basic.show_leds("""
        . . . . .
                . . . # #
                . . . . .
                . . . . .
                . . . # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . #
                . . . . .
                . . . . .
                . . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . . .
                # . . . .
                # . . . .
    """)
    basic.show_leds("""
        . . . . .
                # . . . .
                . # . . .
                . # . . .
                . # . . .
    """)
    basic.show_leds("""
        . . . . .
                # # . . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . # # . .
                # . . # .
                # . . # .
                # . . # .
    """)
    basic.show_leds("""
        . . . . .
                . . # # .
                . # . . #
                . # . . #
                . # . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . # #
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . #
                . . . # .
                . . . # .
                . . . # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . #
                . . . . #
                . . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)

def on_button_pressed_b():
    basic.clear_screen()
    for index in range(2):
        basic.show_leds("""
            . . # # .
                        . . # # .
                        # . # . #
                        . . # . .
                        . # . # .
        """)
        basic.show_leds("""
            . . # # .
                        # . # # #
                        . . # . .
                        . . # . .
                        . # . # .
        """)
        basic.show_leds("""
            . # # . .
                        . # # . .
                        # . # . #
                        . . # . .
                        . # . # .
        """)
        basic.show_leds("""
            . # # . .
                        # # # # .
                        . . # . .
                        . . # . .
                        . # . # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    no_alef()
    no_yud()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

for index2 in range(1):
    basic.clear_screen()
    basic.show_icon(IconNames.GHOST)

def on_forever():
    pass
basic.forever(on_forever)
