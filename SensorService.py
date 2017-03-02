from sense_emu import SenseHat
import time

sense = SenseHat()

def main():
    sense.show_message("Bootup")
    while 1:
        sense.show_message(getsensordata())
        setimage(1)
        time.sleep(5)
        setimage(0)


def getsensordata():
    temp = round(sense.get_temperature(), 1)
    hum = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    return "Temp: {0}, Hum: {1}, Pressure: {2}".format(round(sense.get_temperature(), 1), round(sense.get_humidity(), 1), round(sense.get_pressure(), 1))

def setimage(x):
    r = [255, 0, 0]
    o = [255, 127, 0]
    y = [255, 255, 0]
    g = [0, 255, 0]
    b = [0, 0, 255]
    i = [75, 0, 130]
    v = [159, 0, 255]
    e = [0, 0, 0]

    image = [
        e, e, e, e, e, e, e, e,
        e, e, e, r, r, e, e, e,
        e, r, r, o, o, r, r, e,
        r, o, o, y, y, o, o, r,
        o, y, y, g, g, y, y, o,
        y, g, g, b, b, g, g, y,
        b, b, b, i, i, b, b, b,
        b, i, i, v, v, i, i, b
    ]
    if x is 1:
        sense.set_pixels(image)
    else:
        sense.clear()

if __name__ == "__main__":
    main()