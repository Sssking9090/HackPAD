# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.moduels.encoders import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.moduels.mouse_keys import MouseKeys


# This is the main instance of your keyboard
keyboard = KMKKeyboard()
Encoder_handler = EncoderHandler()
# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(Encoder_handler)
keyboard.moduels.append(MediaKeys)
keyboard.modules.append(MouseKeys)

Encoder_handler.pins = {board.d1, board.d2, none,}  # Define your rotary encoder pins here

# Define your pins here!
PINS = [
    board.D7,   # SW1 (GPIO2)
    board.D8,   # SW2 (GPIO3)
    board.D9,   # SW3 (GPIO4)
    board.D10,   # SW4 (GPIO5)
    board.D5,   # Rotary encoder switch (GPIO21)
]



# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MPLY,
     KC.LCTL(KC.Z), KC.LCTL(KC.Y),
     KC.P, KC.E, ],
]
Encoder_handler.map = [
            ((KC.VOLD, KC.VOLU),),       
                  
            ]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()