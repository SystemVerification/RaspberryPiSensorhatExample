from sense_hat import SenseHat

sense = SenseHat()
sense.show_message("Bootup")
temp = 255
hum = 255
pressure = 255

temp = round(sense.get_temperature(), 1)
hum = rount(sense.get_humidity(), 1)
pressure = round(sense.get_pressure(), 1)

msg = "Temp is {0}, Hum is {1}, Pressure ir {2}".format(temp, hum, pressure)

sense.show_message(msg)