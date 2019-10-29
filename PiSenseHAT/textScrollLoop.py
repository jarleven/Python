from sense_hat import SenseHat

sense = SenseHat()

red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

while True:
    sense.set_rotation(0)
    sense.show_message("Hello world!")

    sense.set_rotation(180)
    sense.show_message("One small step for Pi!", text_colour=red)

    sense.set_rotation(90)
    sense.show_message("Hallo Verden!!", text_colour=green)

    sense.set_rotation(270)
    sense.show_message("10. KL Hospitering", text_colour=blue)
