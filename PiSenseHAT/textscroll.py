from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Hello world!")

sense = SenseHat()
sense.set_rotation(180)

red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

sense.show_message("One small step for Pi!", text_colour=red)

sense.set_rotation(90)
sense.show_message("Hallo Verden!!", text_colour=green)

sense.set_rotation(270)
sense.show_message("Valfag", text_colour=blue)

