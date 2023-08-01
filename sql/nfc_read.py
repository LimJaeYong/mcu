import board
import busio
import adafruit_pn532.i2c as PN532



class nfc:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)

        self.pn532 = PN532.PN532_I2C(self.i2c, debug=False)

        self.pn532.SAM_configuration()


    def run(self):
        print("Waiting for RFID/NFC card.")
        returnUid = ''

        while True:
            self.uid = self.pn532.read_passive_target(timeout=0.5)

            if self.uid is not None:
                #print(self.uid)
                #print("Found card with UID: ", [hex(i) for i in self.uid])
                returnUid = ''.join([chr(i) for i in self.uid])
                print("Found card with UID: ", returnUid)               
                
                return returnUid
            

            print(".")

