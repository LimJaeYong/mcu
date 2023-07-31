import time
import board
import busio
import adafruit_pn532.i2c as PN532

i2c, pn532 = None, None
returnUid = ''


def __init__(self):
    self.i2c = busio.I2C(board.SCL, board.SDA)

    self.pn532 = PN532.PN532_I2C(self.i2c, debug=False)

    self.pn532.SAM_configuration()


def run():
    print("Waiting for RFID/NFC card.")

    while True:
        uid = pn532.read_passive_target(timeout=0.5)

        if uid is not None:
            print("Found card with UID: ", [hex(i) for i in uid])
            print("Found card with UID (string): ",
                  "".join([chr(i) for i in uid]))
            # Convert hex to string
            returnUid.join([chr(i) for i in uid])
        else:
            break

        print(".")

    return returnUid
