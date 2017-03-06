from sense_emu import SenseHat
import time

sense = SenseHat()

def main():
    sense.show_message("Bootup")
    while 1:
        sense.show_message(getsensordata())
        setimage(1)
        time.sleep(30)
        setimage(0)


def getsensordata():
    savedata(round(sense.get_temperature(), 1), round(sense.get_humidity(), 1), round(sense.get_pressure(), 1))
    return "Temp: {0}, Hum: {1}, Pressure: {2}".format(round(sense.get_temperature(), 1), round(sense.get_humidity(), 1), round(sense.get_pressure(), 1))

def savedata(x, e, z):
    a = '/var/www/datafile.json'
    f = open(a, 'w')
    f.write('Temp is %s /n' % x)
    f.write('Humidity is %s /n' % y)
    f.write('Pressure is %s' % z)
    f.close()


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
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e
    ]
    if x is 1:
        sense.set_pixels(image)
    else:
        sense.clear()

if __name__ == "__main__":
    main()
