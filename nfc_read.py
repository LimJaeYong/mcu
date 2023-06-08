import nfc

clf = nfc.ContactlessFrontend('usb')

while True:
    print("카드 스캔....")
    target = clf.sence(RemoteTarget('106A'))
    
    if target is not None:
        print("NFC 정보 : ", target)
        
    time.sleep(0.1)