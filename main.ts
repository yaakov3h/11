input.onPinPressed(TouchPin.P0, function () {
	
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        . . . . .
        # . . # .
        # . # . #
        # . . # .
        . . . . .
        `)
    basic.clearScreen()
})
function no_lamed () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # # . . .
        . # . . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        # . . . .
        # # # . .
        . . # . .
        . # . . .
        # . . . .
        `)
    basic.showLeds(`
        . # . . .
        . # # # .
        . . . # .
        . . # . .
        . # . . .
        `)
    basic.showLeds(`
        . . # . .
        . . # # #
        . . . . #
        . . . # .
        . . # . .
        `)
    basic.showLeds(`
        . . . # .
        . . . # #
        . . . . .
        . . . . #
        . . . # .
        `)
    basic.showLeds(`
        . . . . #
        . . . . #
        . . . . .
        . . . . .
        . . . . #
        `)
}
function no_yud () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # # . . .
        . # . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # # .
        . . . # .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . # #
        . . . . #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Heart)
})
function no_alef () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        # . . . .
        . . . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # . . .
        . # . . .
        # . . . .
        . # . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        # . # . .
        . # . . .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        # . . # .
        . # . # .
        # . # . .
        # . . # .
        `)
    basic.showLeds(`
        . . . . .
        . # . . #
        . . # . #
        . # . # .
        . # . . #
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . . . # .
        . . # . #
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . . . # .
        . . . . #
        . . . # .
        . . . # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . . .
        . . . . #
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
input.onPinPressed(TouchPin.P2, function () {
    music.playMelody("C D E F G A B C5 ", 90)
})
function no_koach () {
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        . # . . .
        . # . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . .
        # # . . .
        . . # . .
        . . # . .
        # # . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        . . . # .
        . . . # .
        . # # . .
        `)
    basic.showLeds(`
        . . . . .
        . . # # .
        . . . . #
        . . . . #
        . . # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . # #
        . . . . .
        . . . . .
        . . . # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        # . . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . .
        # . . . .
        . # . . .
        . # . . .
        . # . . .
        `)
    basic.showLeds(`
        . . . . .
        # # . . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        # . . # .
        # . . # .
        # . . # .
        `)
    basic.showLeds(`
        . . . . .
        . . # # .
        . # . . #
        . # . . #
        . # . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . # #
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . # .
        . . . # .
        . . . # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . #
        . . . . #
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    for (let index = 0; index < 2; index++) {
        basic.showLeds(`
            . . # # .
            . . # # .
            # . # . #
            . . # . .
            . # . # .
            `)
        basic.showLeds(`
            . . # # .
            # . # # #
            . . # . .
            . . # . .
            . # . # .
            `)
        basic.showLeds(`
            . # # . .
            . # # . .
            # . # . #
            . . # . .
            . # . # .
            `)
        basic.showLeds(`
            . # # . .
            # # # # .
            . . # . .
            . . # . .
            . # . # .
            `)
    }
})
input.onPinPressed(TouchPin.P1, function () {
    no_alef()
    no_yud()
})
for (let index = 0; index < 1; index++) {
    basic.clearScreen()
    basic.showIcon(IconNames.Ghost)
}
basic.forever(function () {
	
})
